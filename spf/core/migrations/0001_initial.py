# Generated by Django 3.2.5 on 2021-08-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('print_issn', models.CharField(max_length=9)),
                ('online_issn', models.CharField(max_length=9)),
                ('title', models.CharField(max_length=255)),
                ('abbreviated_title', models.CharField(max_length=255)),
            ],
        ),
    ]