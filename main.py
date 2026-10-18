from fastapi import FastAPI , Query
from pydantic import BaseModel

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # يسمح بلوصول من اي مصدر 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# pydantic  تعريف نموذج البيانات باستخدام
class Student(BaseModel):
    id: int
    name: str
    grade: int 

# قائمه لتخزين البيانات في الذاكره
students = [
    Student(id=1, name="Alice", grade=5),
    Student(id=2, name="Bob", grade=3)
]

#قراءة جميع العناصر
@app.get("/students/")
def read_students():
    return students

#انشاء عنصر جديد
@app.post("/students/")
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student

#تحديد عنصر معين عن طريق ال id باستخدام ال put method
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for i, student in enumerate(students):
        if student.id == student_id:
            students[i] = updated_student
            return updated_student
    return {"message": "Student not found"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(i)
            return deleted_student
    return {"message": "Student not found"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
