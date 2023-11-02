from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def index(request):

    return render(request, 'home.html')


def shoppingSites(request):

    return render(request, 'shopping-sites.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        my_user = User.objects.create_user(username,email,password)
        my_user.save()
        return redirect('Login')
        # else:
        #     return HttpResponse("Please check all fields correctly!!!")

    return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Email and Password is incorrect!!!")

    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
def dashboard(request):

    return render(request, 'user/dashboard.html')


@login_required(login_url='Login')
def shippingHistory(request):

    return render(request, 'user/shippingHistory.html')


@login_required(login_url='Login')
def mypackages(request):

    return render(request, 'user/mypackages.html')


@login_required(login_url='Login')
def orderrequest(request):

    return render(request, 'user/orderrequest.html')


@login_required(login_url='Login')
def customerlist(request):

    return render(request, 'user/customerslist.html')
