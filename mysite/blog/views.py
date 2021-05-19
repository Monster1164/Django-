from django.shortcuts import render
from blog import models
from django.http import HttpResponse

# Create your views here.

def blog_title(request):
    blogs = models.BlogArticles.objects.all()

    return render(request, "blog/titles.html", {"blogs": blogs})
    # return HttpResponse("nihao ")