# Generated by Django 4.0.6 on 2022-11-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referer', '0011_remove_referal_friend_odam'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='menu',
            field=models.IntegerField(null=True),
        ),
    ]
