from django.shortcuts import render,HttpResponse

# Create your views here.

def index(req):
    context = {
        'movies' : ['RDR2','CSRF']
    }
    return render(req,'movies/index.html',context)

def about(req):
    return render(req,'movies/about.html',{})