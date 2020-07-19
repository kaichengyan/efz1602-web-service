# Generated by Django 3.0.8 on 2020-07-19 01:55

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0002_auto_20200719_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='degree_or_job',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='field_or_industry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='primary_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='contact',
            name='school_or_company',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='student_number',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(20160201),
                                                  django.core.validators.MaxValueValidator(20160242)]),
        ),
    ]
