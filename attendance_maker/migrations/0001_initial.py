# Generated by Django 3.0.7 on 2020-06-16 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLASS_CODE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject1', models.IntegerField(default=0)),
                ('subject2', models.IntegerField(default=0)),
                ('subject3', models.IntegerField(default=0)),
                ('subject4', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.CharField(max_length=20)),
                ('B', models.CharField(max_length=20)),
                ('C', models.CharField(max_length=20)),
                ('D', models.CharField(max_length=20)),
                ('E', models.CharField(max_length=20)),
                ('F', models.CharField(max_length=20)),
                ('Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_maker.CLASS_CODE')),
            ],
        ),
        migrations.CreateModel(
            name='Subject_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.CharField(max_length=20)),
                ('B', models.CharField(max_length=20)),
                ('C', models.CharField(max_length=20)),
                ('D', models.CharField(max_length=20)),
                ('E', models.CharField(max_length=20)),
                ('F', models.CharField(max_length=20)),
                ('Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_maker.CLASS_CODE')),
            ],
        ),
        migrations.CreateModel(
            name='Students_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(max_length=20)),
                ('A', models.IntegerField(default=0)),
                ('B', models.IntegerField(default=0)),
                ('C', models.IntegerField(default=0)),
                ('D', models.IntegerField(default=0)),
                ('E', models.IntegerField(default=0)),
                ('F', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=False)),
                ('SubjectName', models.CharField(max_length=20)),
                ('latitude', models.FloatField(default=-1)),
                ('longitude', models.FloatField(default=-1)),
                ('Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_maker.CLASS_CODE')),
            ],
        ),
    ]