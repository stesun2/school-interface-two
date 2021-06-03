#runner.py
from classes.school import School

school = School('Ridgemont High')


# print(school.staff)
# print(school.students)

while True:
    mode = input("What would you like to do?\n"
                "Options:\n"
                "1. List All Students\n"
                "2. View Individual Student <student_id>\n"
                "3. Add a Student\n"
                "4. Remove a Student <student_id>\n"
                "5. Quit\n")

    if mode == '1':
        school.list_students()
    elif mode == '2':
        student_id = input('Enter student id:')
        student = school.find_student_by_id(student_id)
        print(str(student))
    elif mode == '5':
        break

# print(mode)



