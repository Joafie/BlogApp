# Generated by Django 2.0.7 on 2018-07-21 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='contect',
            new_name='content',
        ),
    ]