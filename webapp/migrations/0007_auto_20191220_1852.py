# Generated by Django 3.0.1 on 2019-12-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20191220_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyrule',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]