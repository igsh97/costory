from django.shortcuts import render
from .models import Post
# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    context={"post":posts}
    return render(request,'posts/post_list.html',context)