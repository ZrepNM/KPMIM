# Generated by Django 5.1.3 on 2024-12-20 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REGISTRATION', '0002_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=12)),
                ('Course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='REGISTRATION.course')),
            ],
        ),
    ]
