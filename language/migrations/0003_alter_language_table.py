# Generated by Django 4.2 on 2023-04-18 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0002_alter_language_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='language',
            table='lm_languages',
        ),
    ]
