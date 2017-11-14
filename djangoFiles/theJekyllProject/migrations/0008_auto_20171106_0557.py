# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 05:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theJekyllProject', '0007_auto_20171028_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='repo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='theJekyllProject.Repo'),
            preserve_default=False,
        ),
    ]
