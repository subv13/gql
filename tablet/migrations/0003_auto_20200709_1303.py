# coding=utf-8
# Generated by Django 1.11.28 on 2020-07-09 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tablet", "0002_auto_20200709_1222"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tablet",
            name="name",
            field=models.CharField(help_text="\u0418\u043c\u044f", max_length=255, verbose_name="\u0418\u043c\u044f"),
        ),
        migrations.AlterField(
            model_name="tablet",
            name="workstations",
            field=models.ManyToManyField(
                help_text="\u0421\u0442\u0430\u043d\u0446\u0438\u0438",
                related_name="tablets",
                to="tablet.Workstation",
                verbose_name="\u0421\u0442\u0430\u043d\u0446\u0438\u0438",
            ),
        ),
        migrations.AlterField(
            model_name="workstation",
            name="products",
            field=models.ManyToManyField(related_name="workstations", to="tablet.Product"),
        ),
    ]