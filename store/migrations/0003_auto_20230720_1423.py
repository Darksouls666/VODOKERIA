# Generated by Django 3.2.8 on 2023-07-20 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='telephone',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='zipcode',
        ),
    ]
