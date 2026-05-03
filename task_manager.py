import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            return json.load(f)

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description):
        task = {"id": len(self.tasks) + 1, "task": description, "completed": False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return
        print("\n--- Your Task List ---")
        for t in self.tasks:
            status = "✔" if t['completed'] else "✘"
            print(f"{t['id']}. [{status}] {t['task']}")

    def complete_task(self, task_id):
        for t in self.tasks:
            if t['id'] == task_id:
                t['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as complete!")
                return
        print("Task ID not found.")

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task | 2. List Tasks | 3. Complete Task | 4. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            desc = input("Enter task description: ")
            manager.add_task(desc)
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            tid = int(input("Enter task ID to complete: "))
            manager.complete_task(tid)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()