# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-02 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapplication', '0008_orderdetail_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='sub_total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(blank=True, upload_to='restaurant_logo/'),
        ),
    ]
