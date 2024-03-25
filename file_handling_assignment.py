def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 67890\n")
        print("File created successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File creation process completed.")

def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            contents = file.read()
            print("Contents of my_file.txt:")
            print(contents)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("File appended successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("Appending process completed.")

if __name__ == "__main__":
    create_file()
    read_and_display()
    append_to_file()