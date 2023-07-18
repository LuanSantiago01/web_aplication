# Generated by Django 4.2.2 on 2023-07-11 13:32

from django.db import migrations, models
import django.db.models.deletion
import pictures.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Preco')),
                ('estoque', models.IntegerField(verbose_name='Estoque')),
                ('images', pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, height_field=24, pixel_densities=[1, 2], upload_to='produtos', verbose_name='Imagem', width_field=24)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='slug')),
            ],
            bases=('core.base',),
        ),
    ]
