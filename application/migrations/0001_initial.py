# Generated by Django 3.2.8 on 2022-06-30 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vanne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onoff', models.BooleanField()),
                ('dt', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]