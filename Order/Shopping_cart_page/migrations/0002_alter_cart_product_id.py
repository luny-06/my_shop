# Generated by Django 4.2.5 on 2023-11-09 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping_cart_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
