from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Favorites

def index(request):
    return render(request, 'Movies/index.html')

# remember to install crispy-forms into manage.py for the app to work

# this route registers users and redirects if a user is logged in
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is now active {username}. you may log in!')
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request,'Movies/register.html', {'form': form})



@login_required
def profile(request):
    # this route shows the profile page. Use this to pull data that will be sent to
    # the front end to generate a users profile page

    return render(request, 'Movies/profile.html')


def add(request):
    # use this route to add to a users list (with ajax)*******
    # Favorites(Title = 'x', account = request.user, link = 'y').save()
    # the above line can be filled and used to add objects to the db for the current user
    # then these can just be queried to show on the profile page
    return 1
