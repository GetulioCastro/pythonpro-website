# Generated by Django 3.0.4 on 2020-03-26 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('url', models.URLField()),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
    ]
