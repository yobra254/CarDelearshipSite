# Generated by Django 3.1.5 on 2021-02-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateField(),
        ),
    ]
