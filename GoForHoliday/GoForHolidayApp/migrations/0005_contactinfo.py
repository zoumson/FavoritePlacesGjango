# Generated by Django 3.0.8 on 2020-07-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoForHolidayApp', '0004_auto_20200718_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=2000)),
            ],
        ),
    ]
