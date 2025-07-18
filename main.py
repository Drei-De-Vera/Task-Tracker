#Task Tracker

tasks = []

def add_task():
    title = input("Enter Task Title: ")
    description = input("Enter Task description: ")
    tasks.append({"Title": title, "Description": description, "Done": False})
    print("Task added successfully.\n")

def update_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter the number of task to update: ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("Enter new title (leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            done_status = input("Is the task done? (yes/no): ").strip().lower()

            if new_title:
                tasks[index]['Title'] = new_title
            if new_description:
                tasks[index]['Description'] = new_description
            if done_status in ['yes', 'no']:
                tasks[index]['Done'] = (done_status == 'yes')

            print("Task updated successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Task '{deleted['Title']}' deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def view_task():
    if not tasks:
        print("No task available.\n")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["Done"] else "Pending"
        print(f"{i}. {task['Title']} - {task['Description']} [{status}]")
    print()

def main():
    while True:
        print("=======================")
        print("===Task Tracker Menu===")
        print("=======================")
        print("1. View Task")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select (1-5): ").strip()

        if choice == '1':
            view_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice, Please select a valid option (1-4)")

if __name__ == '__main__':
    main()