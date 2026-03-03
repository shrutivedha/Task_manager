import sqlite3

DB = "tasks.db"

def get_connection():
    return sqlite3.connect(DB)

def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT    NOT NULL,
            done  INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_task(title):
    conn = get_connection()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))  # ✅ Q1
    conn.commit()                                                     # ✅ Q2
    conn.close()
    print(f" Task added: {title}")

def list_tasks():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM tasks")                     # ✅ Q3
    tasks = cursor.fetchall()
    conn.close()
    if not tasks:
        print(" No tasks yet!")
        return
    print("\n─────────────────────────────")
    for task in tasks:
        status = "yes" if task[2] else "no"
        print(f"  [{status}] {task[0]}. {task[1]}")
    print("─────────────────────────────")

def complete_task(task_id):
    conn = get_connection()
    conn.execute("UPDATE tasks SET done=1 WHERE id=?", (task_id,))  # ✅ Q4
    conn.commit()
    conn.close()
    print(" Task completed!")

def delete_task(task_id):
    conn = get_connection()
    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    print(" Task deleted!")

def get_task(task_id):
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task