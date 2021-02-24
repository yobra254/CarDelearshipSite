from django.contrib import admin
from .models import Dealer

class dealerAdmin(admin.ModelAdmin):
    list_display = ('name','email')

# Register your models here.
admin.site.register(Dealer,dealerAdmin)