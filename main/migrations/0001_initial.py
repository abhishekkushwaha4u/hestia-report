# Generated by Django 3.0.4 on 2020-03-25 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateShopRecommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_shop', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('landmark', models.CharField(max_length=20)),
                ('extra_instruction', models.TextField()),
                ('description_of_shop', models.TextField()),
                ('read_by_user', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('reported_by', models.CharField(max_length=255)),
                ('reason', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
