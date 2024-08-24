import sys

#Reading the configuration file and getting the replacements dictionary
def read_conf(read_file):
    replace_dict = {}
    with open(read_file, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            replace_dict[key] = value

    return replace_dict

#Processing and sorting lines of a text file
def correction_lines(read_file, replacements):
    edited_lines = []
    with open(read_file, 'r') as file:
        for line in file:
            correct_line, count_rep = change_line(line, replacements)
            edited_lines.append((correct_line, count_rep))

    edited_lines.sort(key=lambda x: x[1], reverse=True)
    correct_lines = [line for line, _ in edited_lines]

    return correct_lines

#Replacing symbols in a line
def change_line(line, replacements):
    count_rep = 0
    replace_line = line.strip()

    for key, value in replacements.items():
        count = line.count(key)
        replace_line = replace_line.replace(key, value)
        count_rep += count * len(key)

    return replace_line, count_rep

def main():
    #Get command line args, check args count
    if len(sys.argv) != 3:
        print("Error! Print: python replace_script.py 'configuration_file' 'text_file'")
        sys.exit(1)

    conf_file = sys.argv[1]
    text_file = sys.argv[2]

    #Get replacements dictionary
    replacements = read_conf(conf_file)

    #Process lines of a text file
    edited_lines = correction_lines(text_file,replacements)

    #Print result
    with open(text_file, 'w') as file:
        for line in edited_lines:
            print(line)
            file.write(line + '\n')


if __name__ == "__main__":
    main()