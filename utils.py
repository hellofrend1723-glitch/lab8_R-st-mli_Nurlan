#2
def add_vat(price, vat_percent=18):
    return price + price * vat_percent / 100
 
#3 
def build_username(first, last, year=""):
    username = first.lower() + "." + last.lower()
    if year:
        username = username + str(year)
    return username
#5 
def add_bonus(scores, bonus):
    for i in range(len(scores)):
        scores[i] = min(scores[i] + bonus, 100)
def with_bonus(scores, bonus):
    new_scores = []
    for s in scores:
        new_scores.append(min(s + bonus, 100))
    return new_scores
#6 
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
def make_course(code, **details):
    course = {"code": code}
    course.update(details)
    return course
