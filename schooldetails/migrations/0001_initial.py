# Generated by Django 3.2.4 on 2021-06-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('usn', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('sem', models.CharField(default='', max_length=50)),
                ('contact', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
