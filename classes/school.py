from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()
    

    def list_students(self):
        for row in self.students:
            print(f"{row.name} {row.school_id}")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
            else:
                return 'Cannot find id'

