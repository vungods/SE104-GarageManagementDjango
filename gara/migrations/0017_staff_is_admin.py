# Generated by Django 3.0.5 on 2022-05-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gara', '0016_auto_20220527_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]