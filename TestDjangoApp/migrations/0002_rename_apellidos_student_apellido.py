# Generated by Django 4.1.1 on 2022-09-11 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestDjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='apellidos',
            new_name='apellido',
        ),
    ]
