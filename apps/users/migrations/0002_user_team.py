# Generated by Django 3.0.5 on 2020-05-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20200525_1703'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ManyToManyField(blank=True, related_name='team_user', to='teams.Team'),
        ),
    ]
