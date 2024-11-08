task_list = []
def add_task(task_description):
    """Adds a task to the to-do list."""
    if not task_description or not isinstance(task_description, str):
        return "Error: Task description must be a non-empty string."
    task_id = len(task_list) + 1
    task_list.append({"id": task_id, "description": task_description, "status": "Pending"})
    return f"Task '{task_description}' added with ID {task_id}."

