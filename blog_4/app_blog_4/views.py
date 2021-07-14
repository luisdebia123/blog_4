from django.shortcuts import render

from .models import Post, Autor, Categoria
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.




def index(request):
    queryset = request.GET.get('buscar')
    ###########################################################
    # Consulta en Postgrest                                   #
    # SELECT * from app_blog_4_post WHERE estado = 't';       #
    ###########################################################
    posts = Post.objects.filter(estado=True) 
    ###########################################################
    # SELECT * FROM app_blog_4_post                           #
    # WHERE                                                   #
    # description LIKE '%video%'                              #
    # or                                                      #
    # titulo like '%video%';                                 #
    ###########################################################
    if queryset :
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(description__icontains = queryset) 
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_4/index.html',context)




def generales(request):
    queryset = request.GET.get('buscar')
    ############################################################################
    # Consulta en Postgrest                                                    #
    # SELECT * from app_blog_4_post WHERE categoria_id = '1' AND estado = 't'; #
    ############################################################################
    posts = Post.objects.filter(
    estado=True,
    categoria = Categoria.objects.get(nombre__iexact = 'General') 
    )
    ############################################################################
    # SELECT * from app_blog_4_post                                             #
    # WHERE categoria_id = '1'                                                  #
    # AND estado = 't'                                                          #
    # AND description LIKE '%post4%' OR titulo LIKE '%post4%';                  #
    ############################################################################
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) | 
        Q(description__icontains = queryset),
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact = 'General') 
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_4/generales.html',context)


def programacion(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
    estado=True,
    categoria = Categoria.objects.get(nombre__iexact = 'Programación') 
    )
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) | 
        Q(description__icontains = queryset),
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact = 'Programación') 
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_4/programacion.html',context)

def videojuegos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
    estado=True,
    categoria = Categoria.objects.get(nombre__iexact = 'Video Juegos') 
    )
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) | 
        Q(description__icontains = queryset),
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact = 'Video Juegos') 
        ).distinct()

    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_4/videojuegos.html',context)


def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
    estado=True,
    categoria = Categoria.objects.get(nombre__iexact = 'Tecnología') 
    )
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) | 
        Q(description__icontains = queryset),
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnología') 
        ).distinct()
    paginator = Paginator(posts,2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request,'app_blog_4/tecnologia.html',context)






def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
    estado=True,
    categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales') 
    )
    if queryset:
        posts = Post.objects.filter(
        Q(titulo__icontains = queryset) | 
        Q(description__icontains = queryset),
        estado=True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales') 
        ).distinct()
    context = {'posts': posts}
    return render(request,'app_blog_4/tutoriales.html',context)


def detalle_post(request,slug):
    posts = get_object_or_404(Post, slug=slug)
    context = {'posts': posts}
    return render(request,'app_blog_4/post.html',context)