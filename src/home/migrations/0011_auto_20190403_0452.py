# Generated by Django 2.1.5 on 2019-04-03 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("home", "0010_auto_20190403_0446")]

    operations = [
        migrations.AlterField(
            model_name="degree_detail",
            name="notice",
            field=models.TextField(blank=True, null=True),
        )
    ]
