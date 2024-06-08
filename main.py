#
#    CLI TO DO App
#
import json

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
    def add_task(self, task):
        self.tasks_list.append(task)

    # remove task
    def finish_task(self, title):
        for task in self.tasks_list:
            if task.title == title:
                task.toggle_complete()
                return f"{title} is DONE!"
        return f"{title} is not found..."

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
            print("File not found...")


def main():
    tasks = TaskList()

    while True:
        print("\n+++==++~  TODO  ~++==+++")
        print("+ 1. Add a New Task")
        print("+ 2. Complete a Task")
        print("+ 3. View Current Tasks")
        print("+ 4. View Completed Tasks")
        print("+ 5. Save Tasks to file")
        print("+ 6. Load Tasks from file")
        print("+ 7. Exit")

        option = input("\nEnter your choice (1-7): ")

        if option == "1":
            title = input("Enter the Title: ")
            description = input("Enter the Description: ")
            task = Task(title, description, is_complete=False)
            tasks.add_task(task)
            print(f"TODO: {title} added successfully!")

        elif option == "2":
            title = input("Enter the Title: ")
            print(tasks.finish_task(title))

        elif option == "3":
            uncompleted = tasks.get_uncompleted_tasks()
            if uncompleted:
                print("Current Tasks:")
            for task in uncompleted:
                print(f"Title: {task.title}, Description: {task.description}, Completed: {task.is_complete}")
            else:
                print("Currently there are no Active Tasks")

        elif option == "4":
            completed = tasks.get_completed_tasks()
            if completed:
                print("Completed Tasks:")
                for task in completed:
                    print(f"Title: {task.title}, Description: {task.description}, Completed: {task.is_complete}")
            else:
                print("Currently there are no Completed Tasks")

        elif option == "5":
            tasks.save_file()
            print("Tasks saved to .json")

        elif option == "6":
            tasks.load_file()
            print("Tasks loaded from .json")

        elif option == "7":
            print("Goodbye...")
            break

        else:
            print("Invalid option. Please enter a valid option (1-7).")


if __name__ in "__main__":
    main()
