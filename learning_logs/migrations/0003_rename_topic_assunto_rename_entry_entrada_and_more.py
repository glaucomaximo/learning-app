# Generated by Django 5.0.3 on 2024-03-15 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Assunto',
        ),
        migrations.RenameModel(
            old_name='Entry',
            new_name='Entrada',
        ),
        migrations.AlterModelOptions(
            name='entrada',
            options={'verbose_name_plural': 'entradas'},
        ),
    ]
