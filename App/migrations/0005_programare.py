# Generated by Django 5.0.2 on 2024-02-15 23:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_medic_email_alter_pacient_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programare',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Data', models.DateTimeField(default=django.utils.timezone.now)),
                ('Permite_reprogramare', models.BooleanField(default=False)),
                ('Descriere', models.TextField()),
                ('Pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.pacient')),
            ],
        ),
    ]