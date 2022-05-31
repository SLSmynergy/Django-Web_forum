from urllib.parse import urlparse
from django.shortcuts import render, redirect
from service.models import Post, Comment

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')
