# Generated by Django 5.0.4 on 2024-04-09 12:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=13)),
                ('called', models.CharField(choices=[("Bog'lanildi", "Bog'lanildi"), ("Bog'lanilmadi", "Bog'lanilmadi")], default="Bog'lanilmadi", max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
