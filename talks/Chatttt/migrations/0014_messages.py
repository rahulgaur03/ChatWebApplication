# Generated by Django 3.2.8 on 2021-10-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatttt', '0013_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('sender', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('timestamp', models.TimeField()),
            ],
        ),
    ]
