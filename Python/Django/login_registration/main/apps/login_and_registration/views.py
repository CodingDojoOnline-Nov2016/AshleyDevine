from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'login_and_registration/index.html')

def profile(request):
    return render(request, 'login_and_registration/profile.html')

def login(request):
    valid, response = User.objects.login_validation(request.POST)

    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('/')
    else:
        messages.success(request, "Hello, {} {}!".format(response.first_name, response.last_name, response.id))
        request.session['user_id'] = response.id
    return redirect('/profile')

def register(request):
    valid, response = User.objects.registration_validation(request.POST)

    if not valid:
        for error in response:
            messages.error(request, error)
        return redirect('/')
    else:
        messages.success(request, "Hello, {} {}!".format(response.first_name, response.last_name, response.id))
        request.session['user_id'] = response.id
    return redirect('/profile')

def delete(request, id):
    print request.POST
    valid = User.objects.delete_user(id)
    return redirect('/')

def update(request):

    return redirect('')
