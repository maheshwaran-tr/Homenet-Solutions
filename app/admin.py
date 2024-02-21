from django.contrib import admin

from app.models import Product,Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','image','discription')

admin.site.register(Category)
admin.site.register(Product)