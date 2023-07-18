from django.db import models
from pictures.models import PictureField
import django.core.files.storage
# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)


    class META:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    images = PictureField(
        upload_to='produtos',
        aspect_ratios=['800', "1/1", "3/2", "16/9"],
    )
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)

''''''