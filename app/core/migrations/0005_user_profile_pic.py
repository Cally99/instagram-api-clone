# Generated by Django 2.1.5 on 2019-01-16 09:29

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190115_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='avatar.png', upload_to=core.models.image_file_path),
        ),
    ]
