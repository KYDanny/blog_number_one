# Generated by Django 4.2.6 on 2023-10-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]
