import mysql.connector

# Establish MySQL Connection
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your MySQL server host if not localhost
        user="Username",  # Replace with your MySQL username
        password="password",  # Replace with your MySQL password
        database="todo_list"
    )
    return connection


# Create Task
def create_task(task_description):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = "INSERT INTO tasks (task) VALUES (%s)"
    val = (task_description,)

    cursor.execute(sql, val)
    connection.commit()

    print(f"Task '{task_description}' added.")
    cursor.close()
    connection.close()


# Read All Tasks
def read_tasks():
    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if tasks:
        print("Here are your tasks:")
        for task in tasks:
            print(f"[{task[0]}] - {task[1]} | Status: {task[2]} | Created At: {task[3]}")
    else:
        print("No tasks found.")

    cursor.close()
    connection.close()


# update task status
def update_task_status(task_id, new_status):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = "UPDATE tasks SET status = %s WHERE id = %s"
    val = (new_status, task_id)

    cursor.execute(sql, val)
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Task {task_id} updated to '{new_status}'.")
    else:
        print(f"No task found with ID {task_id}.")

    cursor.close()
    connection.close()


# Delete Task
def delete_task(task_id):
    connection = connect_to_db()
    cursor = connection.cursor()

    sql = "DELETE FROM tasks WHERE id = %s"
    val = (task_id,)

    cursor.execute(sql, val)
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Task {task_id} deleted.")
    else:
        print(f"No task found with ID {task_id}.")

    cursor.close()
    connection.close()


# Menu to interact with the tasks
def menu():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task Status\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            create_task(task_description)
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_status = input("Enter new status (pending/completed): ").lower()
            if new_status in ['pending', 'completed']:
                update_task_status(task_id, new_status)
            else:
                print("Invalid status. Please enter 'pending' or 'completed'.")
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the menu() function
if __name__ == "__main__":
    menu()
