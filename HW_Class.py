class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lec_grades:
                lecturer.lec_grades[course] += [grade]
            else:
                lecturer.lec_grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_of_hw(self):
        sum_num = 0
        sum_num_len = 0
        for grade in self.grades.values():
            sum_num_len += len(grade)
            for i in grade:
                sum_num += i
            if sum_num_len:
                return round(sum_num / sum_num_len, 1)
            else:
                return 'Оценок нет'


    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.avg_of_hw()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'

    def __lt__(self, other):
        return self.avg_of_hw() < other.avg_of_hw()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lec_grades = {}
    def avg_of_course(self):
        sum_num = 0
        sum_num_len = 0
        for grade in self.lec_grades.values():
            sum_num_len += len(grade)
            for i in grade:
                   sum_num += i
            if sum_num_len:
                return round(sum_num / sum_num_len, 1)
            else:
                return 'Оценок нет'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_of_course()}'

    def __lt__(self, other):
            return self.avg_of_course() < other.avg_of_course()

class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        super().rate_hw(student,course,grade)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



####################################################################################################
best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.finished_courses += ['Компьютерная грамотность']

best_student2 = Student('Simple','Dimple','male')
best_student2.courses_in_progress += ['Python']
best_student2.finished_courses += ['Кройки и шитья']


cool_mentor1 = Mentor('Some', 'Buddy')
cool_mentor1.courses_attached += ['Python']

cool_mentor2 = Mentor('Jaga','Jagof')
cool_mentor2.courses_attached += ['Python']


beautiful_lecturer1 = Lecturer('Mill','Pops')
beautiful_lecturer1.courses_attached += ['Python']

beautiful_lecturer2 = Lecturer('Natasha','Lutoshkina') # Лучший лектор <3
beautiful_lecturer2.courses_attached += ['Python']


strict_reviewer1 = Reviewer('Vasya','Pupkin')
strict_reviewer1.courses_attached += ['Python']
strict_reviewer1.rate_hw(best_student1,'Python',7)
strict_reviewer1.rate_hw(best_student1,'Python',8)
strict_reviewer1.rate_hw(best_student1,'Python',10)

strict_reviewer2 = Reviewer('Kolobok','Lesnoy')
strict_reviewer2.courses_attached += ['Python']
strict_reviewer2.rate_hw(best_student2,'Python',9)
strict_reviewer2.rate_hw(best_student2,'Python',10)
strict_reviewer2.rate_hw(best_student2,'Python',10)

best_student1.rate_hw(beautiful_lecturer1,'Python',10)
best_student1.rate_hw(beautiful_lecturer1,'Python',3)
best_student1.rate_hw(beautiful_lecturer1,'Python',10)

best_student2.rate_hw(beautiful_lecturer2,'Python',10)
best_student2.rate_hw(beautiful_lecturer2,'Python',10)
best_student2.rate_hw(beautiful_lecturer2,'Python',10)

students_list = [best_student1, best_student2]
def avg_all_student(course, students_list = []):
    all_grades = []
    if students_list:
        for student in students_list:
            for key,value in student.grades.items():
                if key == course:
                    all_grades += value

        return round(sum(all_grades)/len(all_grades),1)


lecturers_list = [beautiful_lecturer1,beautiful_lecturer2]
def avg_all_lectors(course, lecturers_list = []):
    all_grades = []
    if lecturers_list:
        for lecturer in lecturers_list:
            for key,value in lecturer.lec_grades.items():
                if key == course:
                    all_grades += value

        return round(sum(all_grades)/len(all_grades),1)

##################################################################################

print('НАШИ СТУДЕНТЫ:')
print()
print(best_student1)
print()
print(best_student2)
print("Сравнение студентов:")# Задание 3.2 Студенты
print(best_student2 < best_student1)
print()
print('НАШИ ЛЕКТОРА:')
print()
print(beautiful_lecturer1)
print()
print(beautiful_lecturer2)
print("Сравнение лекторов:")# Задание 3.2 Лектора
print(beautiful_lecturer1 < beautiful_lecturer2)
print()
print('НАШИ ПРОВЕРЯЮЩИЕ:')
print()
print(strict_reviewer1)
print()
print(strict_reviewer2)
print()
print(avg_all_student("Python", students_list))#  Ф-ция нахождения средней оценки студентов
print()
print(avg_all_lectors("Python", lecturers_list))#  Ф-ция нахождения средней оценки лекторов