# Generated by Django 3.2.8 on 2022-07-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_vanne_onoff'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapSol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devId', models.IntegerField()),
                ('Temp', models.FloatField(null=True)),
                ('Hum', models.FloatField(null=True)),
                ('Ec', models.FloatField(null=True)),
                ('Sal', models.FloatField(null=True)),
                ('Bat', models.FloatField(null=True)),
                ('dt', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]