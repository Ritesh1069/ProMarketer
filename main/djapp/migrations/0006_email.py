# Generated by Django 4.2.6 on 2023-10-13 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0005_alter_bot_phno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=10000)),
                ('cont', models.CharField(max_length=50000)),
            ],
        ),
    ]
