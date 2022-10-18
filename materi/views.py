from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import Mahasiswa

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def applet(request):
    template = loader.get_template('applet.html')
    return HttpResponse(template.render())
def bab1(request):
    template = loader.get_template('bab1.html')
    return HttpResponse(template.render())
def bab2(request):
    template = loader.get_template('bab2.html')
    return HttpResponse(template.render())
def bab3(request):
    template = loader.get_template('bab3.html')
    return HttpResponse(template.render())
def bab4(request):
    template = loader.get_template('bab4.html')
    return HttpResponse(template.render())
def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())
def mahasiswa(request):
    template = loader.get_template('mahasiswa.html')
    return HttpResponse(template.render())
