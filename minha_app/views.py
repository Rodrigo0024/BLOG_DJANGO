# minha_app/views.py
from django.shortcuts import render
from .models import Post

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
 

