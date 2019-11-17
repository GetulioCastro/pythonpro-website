# Generated by Django 2.2.6 on 2019-11-14 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
            ],
            options={
                'verbose_name': 'sessão',
                'verbose_name_plural': 'sessões',
            },
        ),
    ]