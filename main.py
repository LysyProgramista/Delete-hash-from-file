from sys import argv

def purge(filename : str):
    file = open(filename, 'r')

    old_list = file.readlines()
    new_list = []

    for line in old_list:
        if not line.startswith('#'):
            new_list.append(line)
    return new_list

def write(filename : str, lines : list):
    with open(filename, 'w') as file:
        file.writelines(lines)

filename = argv[1]

write(filename, purge(filename))
