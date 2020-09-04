from django.shortcuts import render

# Create your views here.


def mypage(request):
    return render(request, 'myapp/mypage.html')

def main(request):
    return render(request, 'myapp/main.html')

def myportfolio(request):
    return render(request, 'myapp/myportfolio.html')

def signin(request):
    return render(request, 'myapp/signin.html')

def signup(request):
    return render(request, 'myapp/signup.html')

