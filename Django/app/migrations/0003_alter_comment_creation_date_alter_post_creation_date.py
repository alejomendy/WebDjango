# Generated by Django 4.2.3 on 2023-07-21 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_comment_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
