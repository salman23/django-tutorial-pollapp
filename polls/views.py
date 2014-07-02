from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, This is Poll index")

def detail(request, poll_id):
    return HttpResponse("You are looking at poll id %s" % poll_id)
