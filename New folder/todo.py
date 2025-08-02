import json
import sys
from pathlib import Path

DATA_FILE = Path("todo.json")

def load_tasks():
    if DATA_FILE.exists():

        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["done"] else "✗"
            print(f"{i}. [{status}] {task['description']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Marked task {index} as done.")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['description']}")
    else:
        print("Invalid task number.")

def show_help():
    print("""
Usage:
    python todo.py add "Task description"
    python todo.py list
    python todo.py done [task_number]
    python todo.py delete [task_number]
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1]
        if command == "add" and len(sys.argv) >= 3:
            add_task(" ".join(sys.argv[2:]))
        elif command == "list":
            list_tasks()
        elif command == "done" and len(sys.argv) == 3:
            mark_done(int(sys.argv[2]))
        elif command == "delete" and len(sys.argv) == 3:
            delete_task(int(sys.argv[2]))
        else:
            show_help()
