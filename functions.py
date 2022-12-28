def open_file(filename="todos.txt"):
    with open(filename, "r") as f:
        todos = f.readlines()
        return todos


def write_file(todo_arg,filename="todos.txt"):
    with open(filename, "w") as f:
        f.writelines(todo_arg)
print(__name__)

if __name__ == "__todo_updated__":
    print("hello, i m running functions.py")