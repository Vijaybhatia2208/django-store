from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
  return render(request, 'website/index.html')
  # return HttpResponse("Trying to be better man!")

def Help(request):
  return HttpResponse("Help Trying to be better man!")

def About(request):
  return HttpResponse("About Trying to be better man!")