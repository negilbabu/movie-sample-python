# Generated by Django 4.1.7 on 2023-03-09 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterModelTable(
            name='usermodel',
            table=None,
        ),
    ]
