# Generated by Django 3.1.5 on 2021-01-30 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]
