# Generated by Django 4.0 on 2022-01-01 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('catagory', models.CharField(choices=[('YAC', 'AC'), ('NAC', 'NON-AC'), ('DEL', 'DELUXE'), ('KIN', 'KING'), ('QUE', 'QUEEN')], max_length=30)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]