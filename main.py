#
#    CLI TO DO App
#
import json
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class Task:
    def __init__(self, title: str, description: str, is_complete: bool):
        self.title = title
        self.description = description
        self.is_complete = is_complete

    def toggle_complete(self):
        self.is_complete = not self.is_complete


class TaskList:
    def __init__(self):
        self.tasks_list = []

    def get_completed_tasks(self):
        return [task for task in self.tasks_list if task.is_complete]

    def get_uncompleted_tasks(self):
        return [task for task in self.tasks_list if not task.is_complete]

    # add task
    def add_task(self, task, title):
        if any(task.title == t.title for t in self.tasks_list):
            console.print(f"ERROR: {title} already exists, ya dummy!", style="bold red")
        else:
            self.tasks_list.append(task)
            console.print(f"TODO: {title} added successfully!")

    # remove task
    def finish_task(self, title):
        for task in self.tasks_list:
            if task.title == title:
                task.toggle_complete()
                return console.print(f"{title} is DONE!", style="bold green")
        return console.print(f"{title} is not found...", style="bold red")

    def save_file(self, filename="todo_list.json"):
        data = [{"Task Title:": task.title, "Description:": task.description, "Completed:": task.is_complete} for task in self.tasks_list]
        with open(filename, 'w') as fp:
            fp.write(json.dumps(data))

    def load_file(self, filename="todo_list.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.tasks_list = [Task(task["Task Title:"], task["Description:"], task["Completed:"]) for task in data]
        except FileNotFoundError:
            console.print("File not found...", style="bold red")


def main():
    tasks = TaskList()
    tasks.load_file()

    while True:
        console.print("\n+++==++~  TODO  ~++==+++", style="bold italic cyan")
        console.print("+ 1. Add a New Task", style="italic blue")
        console.print("+ 2. Complete a Task", style="italic white")
        console.print("+ 3. View Current Tasks", style="italic green")
        console.print("+ 4. View Completed Tasks", style="italic green")
        console.print("+ 5. Save Tasks to file", style="italic yellow")
        console.print("+ 6. Load Tasks from file", style="italic yellow")
        console.print("+ 7. Exit", style="italic red")

        option = input("\nEnter your choice (1-7): ")

        if option == "1":
            title = input("Enter the Title: ")
            description = input("Enter the Description: ")
            task = Task(title, description, is_complete=False)
            tasks.add_task(task, title)

        elif option == "2":
            title = input("Enter the Title: ")
            console.print(tasks.finish_task(title))

        elif option == "3":
            uncompleted = tasks.get_uncompleted_tasks()
            if uncompleted:
                console.print("Current Tasks:")
            for task in uncompleted:
                console.print(f"Title: {task.title}, Description: {task.description}, Completed: {task.is_complete}")
            else:
                console.print("Currently there are no Active Tasks")

        elif option == "4":
            completed = tasks.get_completed_tasks()
            if completed:
                console.print("Completed Tasks:")
                for task in completed:
                    console.print(f"Title: {task.title}, Description: {task.description}, Completed: {task.is_complete}")
            else:
                console.print("Currently there are no Completed Tasks")

        elif option == "5":
            tasks.save_file()
            console.print("Tasks saved to .json")

        elif option == "6":
            tasks.load_file()
            console.print("Tasks loaded from .json")

        elif option == "7":
            console.print("Goodbye...")
            break

        else:
            console.print("Invalid option. Please enter a valid option (1-7).")


if __name__ in "__main__":
    main()
