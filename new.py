task_dict = {
    "This is where your tasks will be displayed": "done",
    "try to add a task": "not done",
    "try to delete a task": "not done",
    "try to mark a task as done": "not done",
}

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def calling_action(action):
    if action == 1:
        print_dict(task_dict)
    elif action == 2:
        print("what task would you like to add?")
        new_task = input("Enter your task: ")
        task_dict[new_task] = "not done"
        print_dict(task_dict)
    elif action == 3:
        print_dict(task_dict)
        del_task = input("Enter the task you want to delete: ")
        if del_task in task_dict:
            task_dict.pop(del_task)
            print(f"Task '{del_task}' deleted.")
        else:
            print(f"Task '{del_task}' not found.")
    elif action == 4:
        done_task = input("Enter the task you want to mark as done: ")
        if done_task in task_dict:
            task_dict[done_task] = "done"
            print(f"Task '{done_task}' marked as done.")
        else:
            print(f"Task '{done_task}' not found.")
    else:
        print("Invalid choice. Please try again.")

while True:
    print("""Welcome to the Task Manager! Please choose an action (enter the corresponding number):
    1: View tasks
    2: Add task
    3: Delete task
    4: Mark task as done
    5: Exit
    """)

    action = input("Please enter a number: ")

    if action.isdigit():
        action = int(action)
        if action == 5:  # Exit condition
            print("Exiting Task Manager. Goodbye!")
            break
        calling_action(action)
    else:
        print("Invalid input. Please enter a number.")