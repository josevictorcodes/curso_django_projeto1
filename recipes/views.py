from django.shortcuts import render
#from django.urls import path


# Create your views here.


def home(request):
    """Receives a request and return a html file inside the templates folder"""
    return render(request, 'recipes/pages/home.html')
