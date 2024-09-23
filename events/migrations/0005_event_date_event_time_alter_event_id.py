# Generated by Django 5.0.7 on 2024-07-24 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(default='1999-12-10', max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.CharField(default='23:59:59', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
