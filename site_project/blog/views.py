from django.shortcuts import render
from .models import  Post
from django.utils import timezone

# Create your views here.
def post_list(request):

    all_posts = Post.objects.filter(published_date__lte =  timezone.now()).order_by('published_date')

    return render(
        request,
        "blog/post_list.html",
        {"posts": all_posts}
    )

def post_detail(request,pk):
    post = Post.objects.filter(pk = pk)
    return render(
        request,
        "blog/post_detail.html",
        {'post':post}
    )