from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    path('', views.render_home, name='render_home'),
    # Define more URLs as needed
]
