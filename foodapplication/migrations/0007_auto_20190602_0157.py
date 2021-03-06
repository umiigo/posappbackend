# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-02 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodapplication', '0006_auto_20190602_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapplication.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='foodapplication.Order')),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='order',
        ),
        migrations.DeleteModel(
            name='OrderDetails',
        ),
    ]
