# Generated by Django 4.1.2 on 2022-10-17 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]
