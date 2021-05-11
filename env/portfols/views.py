from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Service, Projects

def index(request):
    services = Service.objects
    projects = Projects.objects
    return render(request,'portfols/index.html',{'services':services,'projects':projects})
