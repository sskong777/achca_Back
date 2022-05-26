# Generated by Django 3.2 on 2022-05-27 03:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_actor_followed_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rank',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
