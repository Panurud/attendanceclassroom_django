from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login , logout

# Create your views here.
def index(request):
    return render(request,"login/login.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'User:{username} | Password:{password}')
        user = authenticate(request, username=username, password=password)
        print("User:",user)
        if user is not None:
            # Log user in
            login(request, user)
            return render(request,"login/home.html")
        else : 
            logout(request)
    return redirect('/')