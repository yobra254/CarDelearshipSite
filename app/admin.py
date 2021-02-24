from django.contrib import admin
from .models import Car

class carAdmin(admin.ModelAdmin):
    list_display = ('brand','dealer','category','power','year')
    list_editable= ('power',)
    list_per_page = 10
    search_fields = ('brand','category','power','year')
    list_filter = ('category','date')

# Register your models here.
admin.site.register(Car,carAdmin)
