from django.urls import path 
from . import views

urlpatterns = [
    path ('login/' , views.render_login , name="render_login"),
    path ('signup/' , views.render_signup , name="render_signup"),
    path ('login/post' , views.handle_login_post , name="handle_login_post"),
    path ('signup/post' , views.handle_signup_post , name="handle_signup_post"),
    path ('handle_email_is_taken/post' , views.handle_email_is_taken , name="handle_email_is_taken"),
    path ('forgetpassword/' , views.render_forget_password , name="render_forget_password"),
]
