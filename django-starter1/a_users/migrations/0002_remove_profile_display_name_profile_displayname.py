# Generated by Django 5.1.1 on 2024-11-03 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='display_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='displayname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]