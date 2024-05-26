import os
import shutil

class FileManager:
    def __init__(self, work_dir):
        self.work_dir = work_dir
        os.chdir(self.work_dir)

    def create_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created successfully.")
        except FileExistsError:
            print(f"Folder '{folder_name}' already exists.")
        except OSError as e:
            print(f"Error: {e}")

    def delete_folder(self, folder_name):
        try:
            os.rmdir(folder_name)
            print(f"Folder '{folder_name}' deleted successfully.")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' not found.")
        except OSError as e:
            print(f"Error: {e}")

    def change_folder(self, folder_name):
        try:
            os.chdir(folder_name)
            print(f"Changed to folder '{folder_name}'.")
        except FileNotFoundError:
            print(f"Folder '{folder_name}' not found.")
        except OSError as e:
            print(f"Error: {e}")

    def move_up(self):
        os.chdir("..")
        print("Moved up to parent folder.")

    def create_file(self, file_name):
        try:
            with open(file_name, 'w'):
                pass
            print(f"File '{file_name}' created successfully.")
        except FileExistsError:
            print(f"File '{file_name}' already exists.")
        except OSError as e:
            print(f"Error: {e}")

    def write_to_file(self, file_name, text):
        try:
            with open(file_name, 'w') as file:
                file.write(text)
            print(f"Text written to '{file_name}' successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except OSError as e:
            print(f"Error: {e}")

    def view_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                print(f"Contents of '{file_name}':")
                print(file.read())
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except IsADirectoryError:
            print(f"'{file_name}' is a directory, not a file.")
        except OSError as e:
            print(f"Error: {e}")

    def delete_file(self, file_name):
        try:
            os.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except IsADirectoryError:
            print(f"'{file_name}' is a directory, not a file.")
        except OSError as e:
            print(f"Error: {e}")

    def copy_file(self, source, destination):
        try:
            shutil.copy(source, destination)
            print(f"File '{source}' copied to '{destination}' successfully.")
        except FileNotFoundError:
            print(f"File '{source}' not found.")
        except IsADirectoryError:
            print(f"'{source}' is a directory, not a file.")
        except OSError as e:
            print(f"Error: {e}")

    def move_file(self, source, destination):
        try:
            shutil.move(source, destination)
            print(f"File '{source}' moved to '{destination}' successfully.")
        except FileNotFoundError:
            print(f"File '{source}' not found.")
        except IsADirectoryError:
            print(f"'{source}' is a directory, not a file.")
        except OSError as e:
            print(f"Error: {e}")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"File '{old_name}' renamed to '{new_name}' successfully.")
        except FileNotFoundError:
            print(f"File '{old_name}' not found.")
        except IsADirectoryError:
            print(f"'{old_name}' is a directory, not a file.")
        except OSError as e:
            print(f"Error: {e}")

    def list_contents(self):
        contents = os.listdir()
        print("Contents of the current directory:")
        for item in contents:
            print(item)

def print_menu():
    print("\nFile Manager Menu:")
    print("1. Create Folder")
    print("2. Delete Folder")
    print("3. Change Folder")
    print("4. Move Up")
    print("5. Create File")
    print("6. Write to File")
    print("7. View File")
    print("8. Delete File")
    print("9. Copy File")
    print("10. Move File")
    print("11. Rename File")
    print("12. List Contents")
    print("0. Exit")

# Пример использования
if __name__ == "__main__":
    work_dir = input("Enter the path to your directory: ")
    file_manager = FileManager(work_dir)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "0":
                print("Exiting...")
                break
            case "1":
                folder_name = input("Enter folder name: ")
                file_manager.create_folder(folder_name)
            case "2":
                folder_name = input("Enter folder name: ")
                file_manager.delete_folder(folder_name)
            case "3":
                folder_name = input("Enter folder name: ")
                file_manager.change_folder(folder_name)
            case "4":
                file_manager.move_up()
            case "5":
                file_name = input("Enter file name: ")
                file_manager.create_file(file_name)
            case "6":
                file_name = input("Enter file name: ")
                text = input("Enter text to write: ")
                file_manager.write_to_file(file_name, text)
            case "7":
                file_name = input("Enter file name: ")
                file_manager.view_file(file_name)
            case "8":
                file_name = input("Enter file name: ")
                file_manager.delete_file(file_name)
            case "9":
                source = input("Enter source file path: ")
                destination = input("Enter destination file path: ")
                file_manager.copy_file(source, destination)
            case "10":
                source = input("Enter source file path: ")
                destination = input("Enter destination file path: ")
                file_manager.move_file(source, destination)
            case "11":
                old_name = input("Enter current file name: ")
                new_name = input("Enter new file name: ")
                file_manager.rename_file(old_name, new_name)
            case "12":
                file_manager.list_contents()
            case _:
                print("Invalid choice. Please enter a valid option.")
