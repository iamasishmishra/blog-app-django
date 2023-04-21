# Generated by Django 4.1.1 on 2023-03-31 13:39

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="contactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=50)),
                ("message", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="post", name="content", field=tinymce.models.HTMLField(),
        ),
    ]
