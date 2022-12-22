# Generated by Django 4.1.3 on 2022-12-20 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('capital', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('major', models.CharField(max_length=80)),
                ('population', models.FloatField(default='no data')),
                ('code_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='world.country')),
            ],
        ),
    ]
