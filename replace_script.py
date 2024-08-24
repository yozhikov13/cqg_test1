import sys

def main():
    if len(sys.argv) != 3:
        print("Error! Print: python replace_script.py 'configuration_file' 'text_file'")
        sys.exit(1)

    conf_file = sys.argv[1]
    text_file = sys.argv[2]

    with open(conf_file, 'r') as file:
        for line in file:
            print(line)

    print("-----")

    with open(text_file, 'r') as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    main()