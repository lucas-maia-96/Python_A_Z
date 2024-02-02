FILENAME = "to_do_list.txt"


def get_todos(filename=FILENAME):
    with open(filename, "r") as file:
        return file.read().splitlines()


def write_todos(list, filename=FILENAME):
    with open(filename, "w") as file:
        for item in list:
            file.write("%s\n" % item)


def print_list(list):
    for index, value in enumerate(list):
        print(f"{index + 1}. {value}")
