# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-02 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapplication', '0007_auto_20190602_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
