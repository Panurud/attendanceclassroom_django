
from django.urls import path 
from attendance_classroom.views import index , signin

urlpatterns = [
    path('',index),
    path('signin',signin)
]
