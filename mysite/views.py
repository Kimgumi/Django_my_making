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



def index(request):
    return HttpResponse("Hello world!")