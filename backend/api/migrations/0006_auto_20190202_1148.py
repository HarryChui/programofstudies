# Generated by Django 2.1 on 2019-02-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_class_mods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='qualification',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]