from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from crm.defines import *

# Create your models here.
class Crm_client(models.Model):
    group_client = models.ForeignKey('Crm_groupclient', verbose_name="Group Client", on_delete=models.CASCADE)
    localisation_country = models.ForeignKey('Localisation_country', verbose_name="Localisation country", on_delete=models.CASCADE)
    localisation_state = models.ForeignKey('Localisation_state', verbose_name="Localization state", on_delete=models.CASCADE)
    localisation_zone = models.ForeignKey('Localisation_zone', verbose_name="Localization zone", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    tecnical_contact = models.EmailField(max_length=70,blank=True, null=True)
    comercial_contact = models.EmailField(max_length=70,blank=True, null=True)
    finance_contact = models.EmailField(max_length=70,blank=True, null=True)
    name = models.CharField(max_length = 144, verbose_name= "Name")
    business_name = models.CharField(max_length = 144, verbose_name= "Business name")
    address_1 = models.CharField(max_length = 144, verbose_name= "Address1")
    identification_type = models.CharField(max_length = 3, null=True, blank=True, choices = TYPE_IDENTIFICATION_CHOICES)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    def __str__(self):
        return self.user

class Crm_service(models.Model):
    area = models.ForeignKey('Crm_area', verbose_name="Crm area", on_delete=models.CASCADE)
    profit_center = models.ForeignKey('Crm_profitcenter', verbose_name="Crm profit center", on_delete=models.CASCADE)
    type_service = models.ForeignKey('Crm_typeservice', verbose_name="Crm type service", on_delete=models.CASCADE)
    name = models.CharField(max_length = 200, verbose_name="Name service")
    comment = models.TextField(verbose_name="Comment")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    def __str__(self):
        return self.name

class Crm_typeservice(models.Model):
    name = models.CharField(max_length = 200, verbose_name="Name type service")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    def __str__(self):
        return self.name

class Crm_area(models.Model):
    name = models.CharField(max_length = 200, verbose_name="Name area")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    def __str__(self):
        return self.name

class Crm_clientservice(models.Model):
    type_service = models.ForeignKey(Crm_service, verbose_name="Crm type service", on_delete=models.CASCADE)
    crm_client = models.ForeignKey(Crm_client, verbose_name="Crm client", on_delete=models.CASCADE)
    profit_center = models.ForeignKey('Crm_profitcenter', verbose_name="Crm profit center", on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True, default=None)
    pay_day = models.IntegerField(null=True)
    type_sla = models.CharField(max_length = 10, null=True, blank=True, choices = TYPE_SLA_CHOICES)
    type_contract = models.CharField(max_length = 10, null=True, blank=True, choices = TYPE_CONTRACT_CHOICES)

class Crm_profitcenter(models.Model):
    name = models.CharField(max_length = 144, verbose_name="Name profit center")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    def __str__(self):
        return self.name

class Crm_groupclient(models.Model):
    name = models.CharField(max_length = 144, verbose_name="Name group client")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update date")

    def __str__(self):
        return self.name

class Localisation_zone(models.Model):
    country = models.ForeignKey('Localisation_country', verbose_name="Localisation country", on_delete=models.CASCADE)
    name = models.CharField(max_length = 144, verbose_name="Name zone")
    code = models.CharField(max_length = 31, verbose_name="Name")
    sort_order = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Localisation_country(models.Model):
    name = models.CharField(max_length = 144, verbose_name="Name country")
    iso_code_2 = models.CharField(max_length = 2, verbose_name="Name iso code 2")
    iso_code_3 = models.CharField(max_length = 3, verbose_name="Name iso code 3")
    sort_order = models.IntegerField()

    def __str__(self):
        return self.name

class Localisation_state(models.Model):
    zone = models.ForeignKey(Localisation_zone, verbose_name="Localisation zone", on_delete=models.CASCADE)
    name = models.CharField(max_length = 144, verbose_name="Name state")
    sort_order = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
