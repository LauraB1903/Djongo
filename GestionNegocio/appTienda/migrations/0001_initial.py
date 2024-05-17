# Generated by Django 4.1.13 on 2024-05-16 22:47

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('catNombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('proCodigo', models.IntegerField(unique=True)),
                ('proNombre', models.CharField(max_length=50)),
                ('proPrecio', models.IntegerField()),
                ('proFoto', models.FileField(blank=True, null=True, upload_to='fotos/')),
                ('proCategoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appTienda.categoria')),
            ],
        ),
    ]