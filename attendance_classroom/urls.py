
from django.urls import path 
from attendance_classroom.views import index

urlpatterns = [
    path('',index)
]
