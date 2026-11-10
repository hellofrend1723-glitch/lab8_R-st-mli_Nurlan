#1
def print_student_card(name, group, year):
    print("Name:", name)
    print("Group:", group)
    print("Year:", year)

print_student_card("Aysel Mammadova", "CE-101", 1)
print_student_card(year=2, name="Kamran Aliyev", group="CE-201")

#4
def make_student(name, score, group=""):
    student = {"name": name, "score": score}
    if group:
        student["group"] = group
    return student

print(make_student("Kamran", 61, "CE-101"))            

students = []
while True:
    name = input("Name (quit to stop): ")
    if name == "quit":
        break
    score = int(input("Score: "))
    students.append(make_student(name, score))

for i in students:
    print(i["name"] + ": " + str(i["score"]))

#5
def add_bonus(scores, bonus):
    for i in range(len(scores)):
        scores[i] = scores[i] + bonus
        if scores[i] > 100:
            scores[i] = 100

def with_bonus(scores, bonus):
    a = scores[:]
    for i in range(len(a)):
        a[i] = a[i] + bonus
        if a[i] > 100:
            a[i] = 100
    return a      

scores = [70, 95, 88, 100]
print(with_bonus(scores, 10))
print(scores)
add_bonus(scores[:], 10)
print(scores)
add_bonus(scores, 10)
print(scores)

#6
def average(*numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def make_course(code, **details):
    course = {}
    course["code"] = code
    for key, value in details.items():
        course[key] = value
    return course

print(average(70, 80, 90))   
print(average(100))          
print(average())             
print(make_course("CE101", title="Fundamentals of Programming", credits=6))

#7 (Bu hissənin işləməsi üçün eyni qovluqda 'utils.py' faylı olmalıdır)

import utils
from utils import average
from utils import build_username as make_user
import utils as u

print(utils.add_vat(200))
print(average(60, 70))
print(make_user("Nigar", "Hasanova"))
print(u.with_bonus([50, 95], 10))

