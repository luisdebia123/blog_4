from django.db import models
from ckeditor.fields import RichTextField

from django.shortcuts import reverse
import uuid                            
from django.utils.text import slugify  
from django.db.models.signals import pre_save  

# Create your models here.

class Categoria (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de la Categoria', max_length= 100, null = False, blank =False)
    estado= models.BooleanField('Categoría Activada/Categoría no Activada', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name ='Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombre del autor', max_length= 255, null= False, blank=False)
    apellidos =  models.CharField('Apellidos del autor', max_length= 255, null= False, blank=False)
    facebook = models.URLField('facebook', null= True, blank=True)
    twitter = models.URLField('twitter', null= True, blank=True)
    instagram = models.URLField('instagram', null= True, blank=True)
    wed = models.URLField('wed', null= True, blank=True)
    correo = models.EmailField('Correo Electronico', blank=False, null=False)
    estado= models.BooleanField('Autor Activo/ No activo', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add= True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0},{1}'.format(self.apellidos, self.nombres)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    description = models.CharField('Descripcion', max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now= False, auto_now_add= True)
    slug = models.SlugField(null=False, blank=False, unique=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.titulo


def set_slug(sender, instance, *args, **kwargs):  
    if instance.slug:
        return 

    id = str (uuid.uuid4())     
    instance.slug = slugify('{}-{}'.format(instance.slug, id[:8])) 

pre_save.connect(set_slug, sender = Post) 


