# Generated by Django 3.0.5 on 2020-05-25 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20200525_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='leader',
            new_name='leader_id',
        ),
    ]
