# Generated by Django 4.0 on 2022-01-01 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelapp.room')),
            ],
        ),
    ]