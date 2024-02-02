# from functions import read_file, write_file, print_list
from modules import functions
import time

now = time.strftime("%b %d, %Y %h:%M")

print("\n*** Welcome to the To Do App ***")
print("It is ", now, "\n")
while (1):
    print("What would you like to do? ")

    user_action = (input(
        "\nType add (todo), show, edit (number), remove (number), or exit: ")).strip().split()
    action = user_action[0].lower()
    rest = ' '.join(user_action[1:])

    match action:

        case "add":
            todos = functions.read_file()
            todos.append(rest)
            functions.write_file(todos)
            print(f"'{rest}' was added to your list\n")

        case "show":
            todos = functions.read_file()
            functions.print_list(todos)

        case "edit":
            todos = functions.read_file()
            try:
                number = int(rest)
                if number > len(todos) or number < 1:
                    print("Invalid number\n")
                else:
                    new_item = input("Enter a new item: ")
                    todos[number - 1] = new_item
                    functions.write_file(todos)
                    print(
                        f"'{todos[number - 1]}' was edited in your list\n")

            except ValueError:
                print("Invalid number\n")
                continue

        case "remove":
            todos = functions.read_file()
            try:
                number = int(rest)
                if number > len(todos) or number < 1:
                    print("Invalid number")
                else:
                    old = todos[number - 1]
                    todos.pop(number - 1)
                    print(
                        f"'{old}' was removed from your list\n")
                    functions.write_file(todos)

            except ValueError:
                print("Invalid number")
                continue
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid input")
            continue

    print("\n")
