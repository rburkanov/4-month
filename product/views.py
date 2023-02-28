from django.http import HttpResponse
import datetime
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello! its my project")
def goodby(request):
    return HttpResponse("Goodby user!")
def nowdate(request):
    return HttpResponse(datetime.datetime.now())