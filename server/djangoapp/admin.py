from django.contrib import admin
from .models import CarMake, CarModel

# Admin Models

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        'car_make',
        'dealer_id',
        'name',
        'type',
        'year'
    )

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )
    inlines = [CarModelInline]
    

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
