# Generated by Django 5.0.7 on 2024-07-24 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_eventapproval_pendingevents_event_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingevents',
            name='organizer',
            field=models.IntegerField(),
        ),
    ]
