from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI(title="Scalable Task API")

# In-memory storage (for demo purposes)
tasks = []

class Task(BaseModel):
    id: str = None
    title: str
    description: str
    completed: bool = False


@app.get("/")
def read_root():
    return {"message": "Scalable Task API is running"}


@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    task.id = str(uuid.uuid4())
    tasks.append(task)
    return task


@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task.id = task_id
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

