# Generated by Django 3.0.1 on 2019-12-20 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20191220_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='accepted',
            new_name='outgoing',
        ),
    ]
