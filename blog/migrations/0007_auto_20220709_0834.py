# Generated by Django 3.1.7 on 2022-07-09 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_article_sub_headline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
