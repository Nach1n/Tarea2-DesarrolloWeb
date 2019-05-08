from django.contrib import admin
from .models import *

# Register your models here
class Crm_clientAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Crm_serviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Crm_typeserviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Crm_areaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Crm_clientserviceAdmin(admin.ModelAdmin):
    list_display = ('amount', 'pay_day', 'type_sla','type_contract',)
    search_fields = ('amount', 'pay_day', 'type_sla','type_contract',) #Campo de busqueda
    list_filter = ('amount', ) #Filtro de busqueda

class Crm_profitcenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Crm_groupclientAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Localisation_zoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'sort_order',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Localisation_countryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code_2', 'iso_code_3',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda

class Localisation_stateAdmin(admin.ModelAdmin):
    list_display = ('name', 'sort_order', 'status',)
    search_fields = ('name',) #Campo de busqueda
    list_filter = ('name', ) #Filtro de busqueda



admin.site.register(Crm_client, Crm_clientAdmin)
admin.site.register(Crm_service, Crm_serviceAdmin)
admin.site.register(Crm_typeservice, Crm_typeserviceAdmin)
admin.site.register(Crm_area, Crm_areaAdmin)
admin.site.register(Crm_clientservice, Crm_clientserviceAdmin)
admin.site.register(Crm_profitcenter, Crm_profitcenterAdmin)
admin.site.register(Crm_groupclient, Crm_groupclientAdmin)
admin.site.register(Localisation_zone, Localisation_zoneAdmin)
admin.site.register(Localisation_country, Localisation_countryAdmin)
admin.site.register(Localisation_state, Localisation_stateAdmin)