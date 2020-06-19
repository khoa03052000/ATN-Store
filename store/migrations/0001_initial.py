# Generated by Django 3.0.7 on 2020-06-19 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptName', models.CharField(max_length=100)),
                ('ptAge', models.IntegerField()),
                ('ptPhone', models.CharField(max_length=15)),
                ('ptIdCard', models.IntegerField()),
                ('ptAddress', models.CharField(max_length=500)),
                ('ptCity', models.CharField(max_length=50)),
                ('ptProvince', models.CharField(max_length=50)),
                ('ptHostpital', models.CharField(max_length=50)),
                ('ptDate', models.DateField()),
                ('ptTime', models.CharField(max_length=50)),
            ],
        ),
    ]
