# Generated by Django 5.0.7 on 2024-07-25 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_alter_eventapproval_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventapproval',
            name='approved',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
