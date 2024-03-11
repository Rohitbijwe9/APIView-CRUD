from django.urls import path
from .views import *


urlpatterns=[
    path('add/',EmployeeView.as_view()),
    path('show/',EmployeeView.as_view()),
    path('update/<int:pk>/',EmployeeView.as_view()),
    path('pupdate/<int:pk>/',EmployeeView.as_view()),
    path('delete/<int:pk>/',EmployeeView.as_view()),
]