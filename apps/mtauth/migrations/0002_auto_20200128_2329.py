# Generated by Django 2.2.9 on 2020-01-28 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='mtuser',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='mtuser',
            old_name='id',
            new_name='uid',
        ),
    ]