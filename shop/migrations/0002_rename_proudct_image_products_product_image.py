# Generated by Django 5.0.6 on 2024-07-10 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='proudct_image',
            new_name='product_image',
        ),
    ]
