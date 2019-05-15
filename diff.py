import sys


def read_config(filename):
    f = open(filename, "r")
    config_dict = {}
    for line in f.readlines():
        line = line.strip()
        if line.startswith("#") or len(line) == 0:
            continue
        line = line.split("=")
        if len(line) != 2:
            print("[+] Weird line:", line)
            continue
        config_dict[line[0]] = line[1]
    return config_dict


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py [config file] [another config file]")
        sys.exit()

    config1 = read_config(sys.argv[1])
    config2 = read_config(sys.argv[2])

    print("="*10, " [DIFFERENT KEYS] ", "="*10, "")
    print("- Only exist in {}:".format(sys.argv[1]))
    for key in config1.keys()-config2.keys():
        print("{}={}".format(key, config1[key]))

    print()

    print("- Only exist in {}:".format(sys.argv[2]))
    for key in config2.keys()-config1.keys():
        print("{}={}".format(key, config2[key]))

    print()

    print("="*10, " [DIFFERENT VALUES] ", "="*10, "")
    print("{:<30}{:<30}{:<30}".format("key", sys.argv[1], sys.argv[2]))
    print("-"*90)
    for key in config1.keys() & config2.keys():
        if config1[key] != config2[key]:
            print("{:<30}{:<30}{:<30}".format(key, config1[key], config2[key]))
