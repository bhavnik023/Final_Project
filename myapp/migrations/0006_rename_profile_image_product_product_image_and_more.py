# Generated by Django 4.2.7 on 2023-12-06 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='profile_image',
            new_name='product_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='profile_price',
            new_name='product_price',
        ),
    ]
