# Generated by Django 4.1.3 on 2022-11-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_post_post_date_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
