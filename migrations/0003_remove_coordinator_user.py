# Generated by Django 4.2.5 on 2023-10-26 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nexus', '0002_remove_application_s_prn_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinator',
            name='user',
        ),
    ]
