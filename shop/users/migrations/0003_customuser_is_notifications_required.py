# Generated by Django 5.0.3 on 2024-04-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_cashback_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_notifications_required',
            field=models.BooleanField(default=True),
        ),
    ]
