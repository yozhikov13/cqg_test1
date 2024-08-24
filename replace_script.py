import sys

def read_conf(read_file):
    replace_dict = {}
    with open(read_file, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            replace_dict[key] = value

    return replace_dict

def main():
    if len(sys.argv) != 3:
        print("Error! Print: python replace_script.py 'configuration_file' 'text_file'")
        sys.exit(1)

    conf_file = sys.argv[1]
    text_file = sys.argv[2]

    replacements = read_conf(conf_file)


if __name__ == "__main__":
    main()