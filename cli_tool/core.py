# cli_tool/core.py

# Global list to store tasks
tasks = []

def add_task(task):
    """
    Adds a task to the tasks list.
    """
    tasks.append(task)  # Append the task to the list
    print(f"Task '{task}' added!")  # Confirm task addition to the user

def view_tasks():
    """
    Displays the list of tasks. If the list is empty, informs the user.
    """
    if not tasks:  # Check if the list is empty
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):  # Enumerate tasks
            print(f"{idx}. {task}")  # Print each task with its number
