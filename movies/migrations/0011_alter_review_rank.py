# Generated by Django 3.2 on 2022-05-24 01:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20220522_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rank',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]