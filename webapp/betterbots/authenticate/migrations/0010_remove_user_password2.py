# Generated by Django 4.0.6 on 2022-08-14 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0009_remove_user_password1_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]