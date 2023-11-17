# Generated by Django 4.2.6 on 2023-11-05 16:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0015_alter_usuario_gym_fecha_inicio_gym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_gym',
            name='fecha_inicio_gym',
            field=models.DateField(default=datetime.datetime(2023, 11, 5, 11, 6, 58, 841156)),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.DateField(default=django.utils.timezone.now)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gymapp.usuario_gym')),
            ],
        ),
    ]