from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import star
from django.urls import reverse
# Create your views here.

def content(request):
    blog_title="my latest posts"
    posts = [ 
        {'title':'post 1','content':'new content of post 1'}
        {'title':'post 2','content':'new content of post 2'}
        {'title':'post 3','content':'new content of post 3'}
        {'title':'post 4','content':'new content of post 4'} ]
    return render(request,'blog.html',{'blog_title':blog_title,'post':posts})


def home(request):
    return HttpResponse("hello guys")


def old(request):
    return redirect("new")


def blogs(request):
    
    return render (request,"blog.html")
def new_url(request):
    return HttpResponse("this is my new website.......")


def index(request):
    hen="New post"
    return render(request,"index.html",{'hen':hen})


def result(request):
    name=request.POST['name']
    email=request.POST['email']
    password=request.POST['password']
    mesg=request.POST['message']
    star.objects.create(name=name,email=email,password=password,mesg=mesg)
    return render(request,'result.html',{'name':name,'email':email,'password':password,'message':mesg,})