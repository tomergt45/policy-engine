# Generated by Django 2.1 on 2019-12-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20191222_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policyrule',
            name='id',
        ),
        migrations.AlterField(
            model_name='policyrule',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
