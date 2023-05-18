from statistics import mean
groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Антон",
        "surname": "Игоревич",
        "exams": ["Английский", "ИС", "КТП"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Андрей",
        "surname": "Петрович",
        "exams": ["Испанский", "ИЯ", "КТС"],
        "marks": [4, 3, 4]
    },
]

def count_mark(students,mark):
    print ("name".ljust(15),"surname".ljust(20), "exams".ljust(20), "marks".ljust(20))
    for student in students:
        marks_list = student['marks']
        result =  (sum(marks_list)/len(marks_list))
        if result >= need:
            print(student["name"].ljust(15), student["surname"].ljust(20), str(student["exams"]).ljust(20), str(student["marks"]).ljust(20))

need = int(input('Input :'))

count_mark(groupmates,need)
