# Generated by Django 4.2 on 2023-04-18 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_alter_genre_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='genre',
            table='lm_genres',
        ),
    ]
