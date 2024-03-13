from . import views
from django.contrib import admin
from django.urls import path
#from travelproject import settings

urlpatterns = [

    path('',views.lazimashirin,name='lazimashirin'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')
]
