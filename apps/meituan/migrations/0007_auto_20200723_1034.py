# Generated by Django 2.2.9 on 2020-07-23 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meituan', '0006_order_merchat_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merchant_id',
            new_name='merchant',
        ),
    ]
