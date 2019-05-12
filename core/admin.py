from django.contrib import admin

from .models import Item, Order, OrderItem
# Register your models here.


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    

admin.site.register(Order)
admin.site.register(OrderItem)