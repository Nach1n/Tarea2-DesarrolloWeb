# Generated by Django 2.1.7 on 2019-05-07 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crm_area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name area')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Crm_client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tecnical_contact', models.EmailField(blank=True, max_length=70, null=True)),
                ('comercial_contact', models.EmailField(blank=True, max_length=70, null=True)),
                ('finance_contact', models.EmailField(blank=True, max_length=70, null=True)),
                ('name', models.CharField(max_length=144, verbose_name='Name')),
                ('business_name', models.CharField(max_length=144, verbose_name='Business name')),
                ('address_1', models.CharField(max_length=144, verbose_name='Address1')),
                ('identification_type', models.CharField(blank=True, choices=[('RUT', 'rut'), ('DNI', 'dni')], max_length=3, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Crm_clientservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, default=None, null=True)),
                ('pay_day', models.IntegerField(null=True)),
                ('type_sla', models.CharField(blank=True, choices=[('8X5', '8x5'), ('24X7', '24x7')], max_length=10, null=True)),
                ('type_contract', models.CharField(blank=True, choices=[('DEFINIDO', 'definido'), ('INDEFINIDO', 'indefinido')], max_length=10, null=True)),
                ('crm_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Crm_client', verbose_name='Crm client')),
            ],
        ),
        migrations.CreateModel(
            name='Crm_groupclient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144, verbose_name='Name group client')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Crm_profitcenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144, verbose_name='Name profit center')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Crm_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name service')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Crm_area', verbose_name='Crm area')),
                ('profit_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Crm_profitcenter', verbose_name='Crm profit center')),
            ],
        ),
        migrations.CreateModel(
            name='Crm_typeservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name type service')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Update date')),
            ],
        ),
        migrations.CreateModel(
            name='Localisation_country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144, verbose_name='Name country')),
                ('iso_code_2', models.CharField(max_length=2, verbose_name='Name iso code 2')),
                ('iso_code_3', models.CharField(max_length=3, verbose_name='Name iso code 3')),
                ('sort_order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Localisation_state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144, verbose_name='Name state')),
                ('sort_order', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localisation_zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144, verbose_name='Name zone')),
                ('code', models.CharField(max_length=31, verbose_name='Name')),
                ('sort_order', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Localisation_country', verbose_name='Localisation country')),
            ],
        ),
        migrations.AddField(
            model_name='localisation_state',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Localisation_zone', verbose_name='Localisation zone'),
        ),
        migrations.AddField(
            model_name='crm_service',
            name='type_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Crm_typeservice', verbose_name='Crm type service'),
        ),
        migrations.AddField(
            model_name='crm_clientservice',
            name='profit_center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Crm_profitcenter', verbose_name='Crm profit center'),
        ),
        migrations.AddField(
            model_name='crm_clientservice',
            name='type_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Crm_service', verbose_name='Crm type service'),
        ),
        migrations.AddField(
            model_name='crm_client',
            name='group_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Crm_groupclient', verbose_name='Group Client'),
        ),
        migrations.AddField(
            model_name='crm_client',
            name='localisation_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Localisation_country', verbose_name='Localisation country'),
        ),
        migrations.AddField(
            model_name='crm_client',
            name='localisation_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Localisation_state', verbose_name='Localization state'),
        ),
        migrations.AddField(
            model_name='crm_client',
            name='localisation_zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Localisation_zone', verbose_name='Localization zone'),
        ),
        migrations.AddField(
            model_name='crm_client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]