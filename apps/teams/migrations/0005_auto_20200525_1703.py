# Generated by Django 3.0.5 on 2020-05-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20200525_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.IntegerField(null=True),
        ),
    ]
