# Generated by Django 4.0 on 2022-01-11 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0002_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='catagory',
            new_name='category',
        ),
    ]
