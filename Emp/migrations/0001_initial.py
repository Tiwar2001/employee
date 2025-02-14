# Generated by Django 5.1.4 on 2025-01-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('Emp_mail', models.EmailField(max_length=254)),
                ('status', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone_number', models.IntegerField(max_length=10)),
            ],
        ),
    ]
