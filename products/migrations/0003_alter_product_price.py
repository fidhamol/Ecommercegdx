# Generated by Django 3.2.18 on 2023-10-04 04:51

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [('products', '0002_remove_product_subcategory_product_category_and_more')]

    operations = [
        migrations.AlterField(
            model_name='product', name='price', field=models.DecimalField(decimal_places=2, max_digits=5)
        )
    ]
