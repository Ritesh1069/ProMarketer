# Generated by Django 4.2.6 on 2023-10-11 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='eadd',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='schd',
        ),
    ]
