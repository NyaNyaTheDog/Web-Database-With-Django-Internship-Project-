# Generated by Django 2.0.7 on 2018-07-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=250)),
                ('License_Keys', models.CharField(max_length=250)),
                ('Machine_ID', models.CharField(max_length=250)),
                ('Machine_Type', models.CharField(max_length=250)),
                ('Asset_Number', models.CharField(max_length=250)),
                ('User', models.CharField(max_length=250)),
                ('Notes_1', models.CharField(max_length=250)),
                ('Notes_2', models.CharField(max_length=250)),
                ('Notes_3', models.CharField(max_length=250)),
            ],
        ),
    ]
