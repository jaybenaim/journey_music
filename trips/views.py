from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from trips.models import *
from journey_music.models import *

def root(request): 
    return redirect('home/')
    
def home(request): 
    return render(request, 'trips_index.html', {
        'trips': Trip.objects.all(), 
    })

def show(request, pk): 
    return render(request, 'show.html', {
        'trip': Trip.objects.get(pk=pk), 
    })

def new(request): 
    form = TripForm()
    context = {'form': form, 'action': '/trips/create'}
    return render(request, 'form.html', context)

def create(request): 
    form = TripForm(request.POST) 
    if form.is_valid(): 
        form.save()
        return redirect('/trips')
    else: 
        context = {'form': form}
        response = render(request, 'form.html', context)
        return HttpResponse(response) 

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            
            user = authenticate(username=username, password=pw)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form
    }) 


def signup(request):
    form = UserCreationForm() 
    context =  {'form': form} 
    return render(request, 'registration/signup.html', context)

def signup_create(request): 
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
        new_user = form.save()
        login(request, new_user)
        return redirect('/')
    else: 
        return render(request, 'registration/signup.html', {'form': form})
