import json

FILENAME = "tasks.json"

tasks = []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)
        print(" Tasks saved!")

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
            for task in data:
                tasks.append(task)
    except FileNotFoundError:
        pass

def get_task_id(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print(" Please enter a valid number!")
        return None

def add_task(title):
    if not title.strip():
        print(" Task title cannot be empty!")
        return
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    print(f" Task added: {title}")
    save_tasks()

def list_tasks():
    if not tasks:
        print(" No tasks yet!")
        return
    print("\n─────────────────────────────")
    for task in tasks:
        status = "yes" if task["done"] else "no"
        print(f"  [{status}] {task['id']}. {task['title']}")
    print("─────────────────────────────")

def complete_task(task_id):
    if task_id is None:
        return
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print(" Task already completed!")
                return
            task["done"] = True
            print(f" Completed: {task['title']}")
            save_tasks()
            return
    print(" Task not found.")

def delete_task(task_id):
    if task_id is None:
        return
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"  Deleted: {task['title']}")
            save_tasks()
            return
    print(" Task not found.")

load_tasks()

if __name__ == "__main__":
    while True:
        print("="*32+"TASK MANAGER"+"="*32)
        print("  1. Add task")
        print("  2. View tasks")
        print("  3. Complete task")
        print("  4. Delete task")
        print("  5. Exit")
        print("="*32)

        choice = input("\nEnter your choice: ")

        if choice == "1":
            title = input("What is your task? ")
            add_task(title)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            task_id = get_task_id("Enter task number to complete: ")
            complete_task(task_id)

        elif choice == "4":
            task_id = get_task_id("Enter task number to delete: ")
            delete_task(task_id)

        elif choice == "5":
            print("\nGoodbye! ")
            break

        else:
            print(" Invalid choice. Pick 1-5.")