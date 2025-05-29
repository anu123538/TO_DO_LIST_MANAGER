import json
import os

FILE_NAME = "todo_data.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📝 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("✅ Task added!")

# Mark task as done
def complete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("✅ Task marked as done.")
    else:
        print("❌ Invalid task number.")

# Delete task
def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"🗑️ Deleted task: {removed['title']}")
    else:
        print("❌ Invalid task number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n📋 ***8To-Do List Manager***")
        print("1. View  your Tasks")
        print("2. Add  your Task")
        print("3. Mark your  Task as Done")
        print("4. Delete your  Task")
        print("5. Exit the app")

        choice = input("select one: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("📁  your Tasks saved. Goodbye Guys!")
            break
        else:
            print("❌ Invalid choice. please enter correctone.")

if __name__ == "__main__":
    main()
