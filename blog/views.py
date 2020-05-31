from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    return render(request, 'blog/detail.html', {'blog': blog_id})
