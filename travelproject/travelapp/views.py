from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def lazimashirin(request):
    return render(request,"index.html")

def about(request):
    return render(request,"index.html")

def contact(request):
    return HttpResponse("Am contact")