# Generated by Django 2.2.10 on 2020-03-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0002_delete_feed'),
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
