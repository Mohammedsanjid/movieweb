# Generated by Django 4.2.3 on 2023-07-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(max_length=200),
        ),
    ]
