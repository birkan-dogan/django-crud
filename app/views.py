from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    return render(request, "app/index.html")

# read process

def student_list(request):
     students = Student.objects.all()
     context = {
         "students":students
     }
     return render(request, "app/student_list.html",context)
