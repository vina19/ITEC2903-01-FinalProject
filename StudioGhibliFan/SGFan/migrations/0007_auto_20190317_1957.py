# Generated by Django 2.1.7 on 2019-03-18 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGFan', '0006_auto_20190317_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sgmovies',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]