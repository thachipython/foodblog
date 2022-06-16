# Generated by Django 3.2.12 on 2022-03-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='picture')),
                ('des', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
