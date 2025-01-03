# cli_tool/main.py

from cli_tool.core import add_task, view_tasks

def main():
    """
    Runs the main loop of the program, displaying a menu and responding to user choices.
    """
    while True:
        print("\nWelcome to the Simple To-Do List!")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":  # Add task
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "2":  # View tasks
            view_tasks()
        elif choice == "3":  # Exit
            print("Goodbye!")
            break
        else:  # Handle invalid input
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  # Start the program
