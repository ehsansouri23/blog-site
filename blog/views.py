from django.shortcuts import render
from blog.models import BlogPost
from django.http import HttpResponse


def blog_posts(request, blog_id):
    # return render(request, 'blog/posts.html', {
    #     'Post': BlogPost.objects.filter(pk=blog_id)
    # })
    if request.POST:
        # return render(request ,'blog/posts.html')
        return HttpResponse("Post", content_type="text/plain")
    else:
        return render(request, 'blog/get.html')