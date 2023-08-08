from django.shortcuts import render ,redirect,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from .models import User
import json

# Create your views here.

def render_login (request):
    return render(request , 'registration/login.html')

def render_signup (request):
    return render(request , 'registration/signup.html')

def render_forget_password (request):
    return render(request , 'registration/forgetpassword.html')

def handle_login_post (request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        all_users = User.objects.all()  
        found = False  
        for user in all_users:
            if user.email == email :
                found = True
                if user.password == password:
                    return redirect('home')# hnaaa           <-------
                else : return JsonResponse({"msg" : "Wrong Password"})
        if not found : return JsonResponse({"msg" : "Email not found"})

        return JsonResponse({"is_Taken" : True})
    else : return redirect('/registration/login')

def handle_email_is_taken(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get("email")
        user = User.objects.filter(email=email).first()
        if user : return JsonResponse({"is_Taken" : True})
        else : return JsonResponse({"is_Taken" : False})
    else : return redirect('/registration/signup')

def handle_signup_post (request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        new_user = User.objects.create(email=email, password=password)
        new_user.save()
        return render(request , 'home.html',{'user': new_user}) # redirect home
    else : return redirect('/registration/signup')




