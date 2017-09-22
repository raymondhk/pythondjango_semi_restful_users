from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.
def indexredirect(request):
    return redirect('/users/')

def index(request):
    return render(request, ('users/index.html'), { "users": User.objects.all()})

def new(request):
    return render(request, ('users/new.html'))

def info(request, id):
    try:
        user = User.objects.get(id=id)
    except:
        return redirect('/')
    return render(request, ('users/info.html'), { "user": user })

def edit(request, id):
    try:
        user = User.objects.get(id=id)
    except:
        return redirect('/')
    return render(request, ('users/edit.html'), { "user": user })

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new/')
    else:
        user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        user.save()
        print user
        return redirect('/')

def update(request, id):
    user = User.objects.get(id=id)
    if len(request.POST['first_name']) == 0:
        print user.first_name
    else:    
        user.first_name = request.POST['first_name']
    if len(request.POST['last_name']) == 0:
        print user.last_name
    else:
        user.last_name = request.POST['last_name']
    if len(request.POST['last_name']) == 0:
        print user.email
    else:
        user.email = request.POST['email']
    user.save()
    print user
    return redirect('/')

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')