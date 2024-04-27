from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

   

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    instructor_name = models.CharField(max_length=100)
    schedule = models.ForeignKey('CourseSchedule', on_delete=models.CASCADE)
    prerequisites = models.CharField(max_length=100, default="some default value")
    capacity = models.PositiveIntegerField()

class CourseSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    days = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=10)


class StudentRegistration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
