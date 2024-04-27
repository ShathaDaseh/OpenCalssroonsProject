from django.shortcuts import render,redirect
from .models import  Student,Course,CourseSchedule,StudentRegistration


def home(request):
 
    if request.method == 'POST':
        course_code = request.POST.get('course_code')
        course_name = request.POST.get('course_name')
        description = request.POST.get('description')
        instructor_name = request.POST.get('instructor_name')
        prerequisites = request.POST.get('prerequisites')
        capacity = request.POST.get('capacity')
        days = request.POST.get('days')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        room_no = request.POST.get('room_no')
        
        # Create CourseSchedule object
        schedule = CourseSchedule.objects.create(days=days, start_time=start_time, end_time=end_time, room_no=room_no)
        
        # Create Course object
        course = Course.objects.create(course_code=course_code, course_name=course_name, 
                                       description=description, instructor_name=instructor_name, 
                                       prerequisites=prerequisites, capacity=capacity, schedule=schedule)
        
        return redirect('home')  # Redirect to the same page after form submission
    else:
      return render(request, 'home.html')

