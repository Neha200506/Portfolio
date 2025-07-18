from django.shortcuts import render

def home(request):
    skills = ['C++', 'Python', 'Java', 'HTML & CSS', 'JavaScript (Basics)']
    frameworks = ['Django (Beginner)', 'Tailwind CSS', 'Bootstrap (Basics)', 'VS Code', 'Git', 'GitHub']

    return render(request, 'portfolio/home.html', {
        'skills': skills,
        'frameworks': frameworks
    })
