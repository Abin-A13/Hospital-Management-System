# Generated by Django 3.2.2 on 2021-06-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalAPP', '0004_auto_20210622_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='discrpition',
            field=models.TextField(default=34, max_length=200),
            preserve_default=False,
        ),
    ]