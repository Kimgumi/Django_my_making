from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def startpage(request):
    return render(
        request,
        'mysite/introduceMe.html'
    )

def landing(request):
    return render(
        request,
        'mysite/write/landing.html'
    )

def resume(request):
    return render(
        request,
        'mysite/write/Resume.html'
    )

def write(request):
    return render(
        request,
        'mysite/write/Write.html'
    )