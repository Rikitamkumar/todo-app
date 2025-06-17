# todo.py

todo_list = []

def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added!")
    elif choice == '2':
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
