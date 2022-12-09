from django.shortcuts import render

def home(request):
    return render(request, 'schedule/Welcome_Page.html')
