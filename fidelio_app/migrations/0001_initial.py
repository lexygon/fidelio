# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FidelioImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.CharField(blank=True, default='N/A', max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, default='N/A', max_length=100, null=True)),
                ('samplerate', models.IntegerField(blank=True, default=44100, null=True)),
                ('md5', models.CharField(blank=True, default='N/A', max_length=100, null=True)),
                ('gif', models.CharField(blank=True, default='N/A', max_length=100, null=True)),
                ('images', models.ManyToManyField(to='fidelio_app.FidelioImage')),
            ],
            options={
                'verbose_name': 'Sound',
                'verbose_name_plural': 'Sounds',
            },
        ),
    ]
