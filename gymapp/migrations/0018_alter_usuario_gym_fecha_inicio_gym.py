# Generated by Django 4.2.6 on 2023-11-05 16:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0017_alter_usuario_gym_fecha_inicio_gym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_gym',
            name='fecha_inicio_gym',
            field=models.DateField(default=datetime.datetime(2023, 11, 5, 11, 38, 53, 265711)),
        ),
    ]
