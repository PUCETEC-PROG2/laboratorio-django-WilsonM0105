# Generated by Django 5.1.4 on 2025-01-18 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('F', 'Fuego'), ('L', 'Lagartija'), ('E', 'Eléctrico'), ('A', 'Agua'), ('T', 'Tierra')], max_length=30),
        ),
    ]
