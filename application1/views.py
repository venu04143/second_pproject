from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def name(request):
    return HttpResponse('<h1><marquee>my name is venu gopal</h1></marquee>')