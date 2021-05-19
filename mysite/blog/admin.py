from django.contrib import admin

# Register your models her
from blog.models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    # 表单展示
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["publish", "author"]


admin.site.register(BlogArticles, BlogArticlesAdmin)
