from django.urls import path
from app_bs import views

app_name = 'app_bs'

urlpatterns=[
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]