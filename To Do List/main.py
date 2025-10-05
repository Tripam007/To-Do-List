# Simple To-Do List in Python

todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Remove All Tasks")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty! 📝")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added successfully! ✅")
    else:
        print("You can't add an empty task! ⚠️")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' removed successfully! 🗑️")
            else:
                print("Invalid task number! ❌")
        except ValueError:
            print("Please enter a valid number! ❌")
            
            
def delete_all_tasks():
    if todo_list:
        confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()
        if confirm == "yes":
            todo_list.clear()
            print("All tasks have been deleted! 🗑️")
            print("You have completed your goal!😊")
        else:
            print("Deletion cancelled. ❌")
    else:
        print("Your to-do list is already empty! 📝")
    

show_menu()
# Main loop
while True:
    choice = input("Choose an option (1-5): ").strip()
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        delete_all_tasks()
    elif choice == "5":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice! Please enter 1-5. ❌")
