# Generated by Django 4.2.2 on 2023-10-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=130, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]