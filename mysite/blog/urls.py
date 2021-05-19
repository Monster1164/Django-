from django.urls import path
from . import views

urlpatterns = [

    # re_path(r'^$',views.blog_title),
    path("", views.blog_title, name="blog_title"),

]
