# Generated by Django 3.2.8 on 2021-10-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myblogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=25)),
                ('blog_desc', models.CharField(max_length=100)),
                ('publish_date', models.DateField()),
            ],
        ),
    ]