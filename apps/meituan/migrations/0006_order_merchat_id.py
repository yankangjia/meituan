# Generated by Django 2.2.9 on 2020-07-22 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meituan', '0005_auto_20200722_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='merchant_id',
            field=models.ForeignKey(default=31, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='meituan.Merchant'),
            preserve_default=False,
        ),
    ]