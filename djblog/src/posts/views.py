from django.shortcuts import render
from .models import Post

def post_list(request):
    data = Post.objects.all()
    return render(request,'posts/posts.html',{'posts':data})
# Create your views here.

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request,'posts/detail.html',{'post':data})
