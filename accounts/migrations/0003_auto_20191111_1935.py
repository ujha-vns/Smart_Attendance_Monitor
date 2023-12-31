# Generated by Django 2.2.6 on 2019-11-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191106_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='latitude',
            field=models.FloatField(default=-1),
        ),
        migrations.AddField(
            model_name='students',
            name='longitude',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='latitude',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='longitude',
            field=models.FloatField(default=-1),
        ),
    ]
