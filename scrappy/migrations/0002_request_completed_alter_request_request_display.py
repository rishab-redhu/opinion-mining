# Generated by Django 4.0.3 on 2022-04-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrappy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_display',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
