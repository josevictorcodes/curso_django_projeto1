from django.shortcuts import render
#from django.urls import path
from django.http import HttpResponse

# Create your views here.


def home(request):
    """Receives a request and return a html file inside the templates folder"""
    return render(request, 'recipes/home.html')

def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return render(request, 'recipes/sobre.html')
