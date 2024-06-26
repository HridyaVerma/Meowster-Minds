# Generated by Django 5.0.2 on 2024-03-28 07:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment_details',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('appointment_Time', models.TimeField()),
                ('reason_for_visit', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='patient_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
