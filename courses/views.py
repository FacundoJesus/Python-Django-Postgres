from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects
    return render(request, 'courses/index.html',{'courses':courses})

def detail(request,course_id):
    course_detail = get_object_or_404(Course,pk=course_id)
    return render(request, 'courses/detail.html', {'course':course_detail})
