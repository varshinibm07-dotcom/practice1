# student management system 
student={}
n=int(input("enter the number of student: "))
for i in range(n):
    name=(input("enter a student name: "))
    marks=int(input("enter the student marks: "))
    student.setdefault(name,marks)
print(student)
print(max(student,key=student.get))