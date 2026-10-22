from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    context = {
        'name': 'maneth baco',
        'student_id': '2015-03949',
    }
    return render(request, 'about.html', context)