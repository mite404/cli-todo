#
#    CLI TO DO App
#

class Task:
    def __init__(self, title: str, description: str, is_complete: bool):
        self.title = title
        self.description = description
        self.is_complete = is_complete

    def toggle_complete(self):
        self.is_complete = not self.is_complete


class TaskList:
    def __init__(self):
        self.current_tasks = []
        self.completed_tasks = []

    # add
    def add_task(self, task):
        self.current_tasks.append(task)

    # remove
    def finish_task(self, title):
        for task in self.current_tasks:
            if task.title == title:
                task.toggle_complete()
                self.current_tasks.remove(task)
                self.completed_tasks.append(task)
                return f"{title} has been moved to DONE!"
        return f"{title} is not found..."


def main():
    current = TaskList()

    while True:
        print("\n+++==++~  TODO  ~++==+++")
        print("+ 1. Add a New Task")
        print("+ 2. Complete a Task")
        print("+ 3. View Current Tasks")
        print("+ 4. View Completed Tasks")
        print("+ 5. Exit")

        option = input("Enter your choice (1-5): ")

        if option == "1":
            title = input("Enter the Title: ")
            description = input("Enter the Description: ")
            task = Task(title, description, is_complete=False)
            current.add_task(task)
            print(f"TODO: {title} added successfully!")

        elif option == "2":
            title = input("Enter the Title: ")
            print(current.finish_task(title))

        elif option == "3":
            for task in current.current_tasks:
                print(f"Title: {task.title}, Description: {task.description}, Completed: {task.is_complete}")

        elif option == "4":
            if current.completed_tasks:
                for task in current.completed_tasks:
                    print(f"Title: {task.title}, Description: {task.description}, Completed: {task.is_complete}")
            else:
                print("Currently there are no Completed Tasks")

        elif option == "5":
            print("Goodbye...")
            break

        else:
            print("Invalid option. Please enter a valid option (1-5).")


if __name__ in "__main__":
    main()
