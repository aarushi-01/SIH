# Generated by Django 4.0.4 on 2022-06-03 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_studata_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studata',
            name='contact',
            field=models.TextField(default='', verbose_name='contact'),
        ),
    ]
