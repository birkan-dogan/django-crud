from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
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


# create process (POST)

def student_add(request):
    form = StudentForm()
    if (request.method == "POST"):
        form = StudentForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect("list")

    context = {
        "form":form
    }
    return render(request, "app/student_add.html",context)


# update process

def student_update(request,id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if(request.method == "POST"):
        form = StudentForm(request.POST,instance=student)  # here is important
        if(form.is_valid()):
            form.save()
            return redirect("list")
    context = {
        "form":form
    }
    return render(request, "app/student_update.html",context)