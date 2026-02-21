# Scalable Task Management API

## Overview
A RESTful backend API built using FastAPI for managing tasks.
This project demonstrates clean architecture principles, modular design, and scalable backend structure.

## Features
- Create, Read, Update, Delete (CRUD) tasks
- UUID-based task identification
- Request validation with Pydantic
- Interactive API documentation (Swagger UI)
- Dockerized deployment setup

## Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Docker

## Project Structure
```
scalable-task-api/
│
├── app/
│   └── main.py
│
├── requirements.txt
├── Dockerfile
└── README.md
```

## Running Locally

### 1. Clone the repository
```
git clone <your-repo-url>
cd scalable-task-api
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the server
```
uvicorn app.main:app --reload
```

### 4. Access API Docs
```
http://127.0.0.1:8000/docs
```

## Future Improvements
- Integrate PostgreSQL
- Add authentication (JWT)
- Add unit tests
- Deploy to cloud (AWS/GCP/Azure)

---

## Author
Backend API project demonstrating scalable architecture principles.
