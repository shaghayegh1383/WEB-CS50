from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"first/index.html")

def greet(request , name):
    return HttpResponse(f"Hello,{name}")