# Generated by Django 3.2.18 on 2023-10-20 07:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('products', '0004_alter_product_price')]

    operations = [
        migrations.AlterModelOptions(name='category', options={'verbose_name_plural': 'Categories'}),
        migrations.AlterModelOptions(name='subcategory', options={'verbose_name_plural': 'SubCategories'}),
    ]
