from django.shortcuts import render, get_object_or_404
from REGISTRATION.models import Course, Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Index view
def index(request):
    allcourse = Course.objects.all()  # Fetch all courses to pass to the index
    context = {
        'allcourse': allcourse,
    }
    return render(request, "index.html", context)

# Course view
def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        # Save course to the database
        Course.objects.create(code=c_code, description=c_desc)
        message = "Data Saved Successfully"
    else:
        message = ""

        allcourse = Course.objects.all()
        context = {
            'message': message,
            'allcourse': allcourse,
        }
    return render(request, 'course.html', context)

# Mentor view
def mentor(request):
    if request.method == 'POST':
        m_cd = request.POST['ID']
        m_name = request.POST['NAME']
        m_email = request.POST['EMAIL']
        # Save mentor to the database
        Mentor.objects.create(code=m_cd, name=m_name, mail=m_email)
        message = "Data Saved Successfully"
    else:
        message = ""

    allmentor = Mentor.objects.all()
    context = {
        'message': message,
        'allmentor': allmentor,
    }
    return render(request, 'mentor.html', context)

# Search view
def search(request):
    c_code = request.GET.get('c_code')
    data = Course.objects.filter(code=c_code.upper()) if c_code else None
    data1 = Mentor.objects.filter(code=c_code.upper()) if c_code else None

    context = {
        'data': data,
        'data1': data1,
    }
    return render(request, "search.html", context)

# Update course view
def update_course(request, c_code):
 
    data = Course.objects.get(code=c_code)
    allcourse = Course.objects.all()  # Fetch all courses to pass to the index
    context = {
        'data': data,
        "allcourse" : allcourse
        }
    return render(request, "update_course.html", context)

# Save updated course view
def save_update_course(request, c_code):
    if request.method == 'POST':
        c_desc = request.POST['desc']
        # Fetch and update course description
        data = get_object_or_404(Course, code=c_code)
        data.description = c_desc
        data.save()
        return HttpResponseRedirect(reverse("course"))