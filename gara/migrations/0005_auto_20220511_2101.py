# Generated by Django 3.0.5 on 2022-05-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gara', '0004_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default='AnonymousUser', max_length=15),
        ),
    ]
