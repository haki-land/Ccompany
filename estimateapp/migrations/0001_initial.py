# Generated by Django 3.2.9 on 2021-11-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstimateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=13)),
                ('area', models.IntegerField()),
                ('types', models.CharField(choices=[('apt', '아파트'), ('house', '주택'), ('store', '상가')], max_length=50)),
                ('input_estimateimage', models.ImageField(upload_to='input_estimate')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('df', models.CharField(max_length=500)),
                ('construction', models.JSONField()),
                ('detail', models.JSONField()),
            ],
        ),
    ]
