# Generated by Django 3.2.5 on 2023-01-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mirai', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AddField(
            model_name='company',
            name='cLocation',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
