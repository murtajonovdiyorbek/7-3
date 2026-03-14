from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
admin.site.register([Category, ProductImage])

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'get_image')
    list_editable = ('category',)
    list_filter = ('category',)
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'category__name')

    inlines = [
        ProductImageInline
    ]

    @admin.display(description="image")
    def get_image(self, obj):
         return mark_safe(f"<img src='{obj.get_image()}' style='width: 150px;'>")


