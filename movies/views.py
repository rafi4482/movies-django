from django.shortcuts import render,HttpResponse

# Create your views here.

def index(req):
    return render(req,'movies/index.html',{})

def about(req):
    return render(req,'movies/about.html',{})