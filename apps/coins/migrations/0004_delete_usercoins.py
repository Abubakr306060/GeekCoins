# Generated by Django 5.0.1 on 2024-01-22 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0003_alter_usercoins_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserCoins',
        ),
    ]
