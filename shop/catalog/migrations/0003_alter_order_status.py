# Generated by Django 5.0.3 on 2024-04-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_cart_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('In Process', 'In Process'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Received', 'Received'), ('Refused', 'Refused')], default='In Process', max_length=100),
        ),
    ]
