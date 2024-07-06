# Generated by Django 5.0.2 on 2024-02-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Nume', models.CharField(max_length=255)),
                ('Prenume', models.CharField(max_length=255)),
                ('CNP', models.CharField(max_length=13, unique=True)),
                ('Parafa_medic_de_familie', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
