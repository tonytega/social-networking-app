from django.contrib import admin
from .models import UserDetail,UserPost,Tag
# Register your models here.
admin.site.register(UserPost)
admin.site.register(UserDetail)
admin.site.register(Tag)