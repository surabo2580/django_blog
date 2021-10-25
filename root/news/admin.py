from django.contrib import admin
from news.models import Post,NewsComment

# Register your models here.
admin.site.register((Post,NewsComment))
