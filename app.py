from flask import Flask, jsonify, request
from database import create_table, add_task, list_tasks, complete_task, delete_task, get_task
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
create_table()   # create table when server starts

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = __import__('sqlite3').connect("tasks.db")
    cursor = conn.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    tasks = [{"id": r[0], "title": r[1], "done": bool(r[2])} for r in rows]
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    add_task(data["title"])
    return jsonify({"message": "Task added!"}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def finish_task(task_id):
    complete_task(task_id)
    return jsonify({"message": "Task completed!"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted!"})

if __name__ == "__main__":
    app.run(debug=True)
