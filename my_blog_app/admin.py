from django.contrib import admin
from my_blog_app.models import Post, BlogComment

admin.site.register((Post,BlogComment))