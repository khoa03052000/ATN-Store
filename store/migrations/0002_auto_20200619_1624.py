# Generated by Django 3.0.7 on 2020-06-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='ptAddress',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ptAge',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ptCity',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ptDate',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ptHostpital',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ptPhone',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ptProvince',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ptTime',
        ),
        migrations.AddField(
            model_name='patient',
            name='ptPrice',
            field=models.FloatField(default=20.0),
            preserve_default=False,
        ),
    ]
