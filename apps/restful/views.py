# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from django.urls import reverse
from .models import Users

# Create your views here.
def index(request):
    context = {
        "users": Users.objects.all(),
    }
    return render(request, 'restful/index.html', context=context)

def new(request):
    return render(request, 'restful/new.html')

def create(request):
    if Users.objects.validator(request.POST) == False:
        return HttpResponse("email already exists")
    else: 
        Users.objects.create(name=request.POST['name'],email=request.POST['email'])
        user_id = Users.objects.get(email=request.POST['email'])
        return redirect(reverse('show',args=[user_id.id]))

def show(request,id):
    context = {
        "user":Users.objects.get(id=id),
    }
    return render(request, 'restful/show.html', context)

def delete(request,id):
    Users.objects.get(id=id).delete()
    return redirect('/users')

def edit(request,id):
    context = {
        "user":Users.objects.get(id=id),
    }
    return render(request, 'restful/edit.html', context)

def update(request,id):
    u = Users.objects.get(id=request.POST['id']) 
    u.name = request.POST['name']
    u.email = request.POST['email']
    u.save()
    return redirect('/users')