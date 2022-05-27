from django.contrib import admin
from .models import *

class detUserTech(admin.ModelAdmin):
    list_display = ('id', 'name', 'perfilFK')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

class detDevices(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date', 'status', 'image')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

class detComments(admin.ModelAdmin):
    list_display = ('id', 'description', 'date', 'userFK', 'deviceFK')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 10

class detPerfil(admin.ModelAdmin):
    list_display = ('id', 'perfil')
    list_display_links = ('id',)
    search_fields = ('perfil',)
    list_per_page = 10

admin.site.register(UserTech, detUserTech)
admin.site.register(Devices, detDevices)
admin.site.register(Comments, detComments)
admin.site.register(Perfil, detPerfil)
