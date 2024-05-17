from django.shortcuts import render,redirect
from appTienda.models import Categoria, Producto
from django.http import JsonResponse
from django.db import Error
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from bson import ObjectId
# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def vistaAgregarCategoria(request):
    return render(request,"agregarCategoria.html")

def agregarCategoria(request):
    try:
        nombre = request.POST['nombre']
        categoria = Categoria(catNombre = nombre)
        categoria.save()
        mensaje = "Categoria Agregado Correctamente"
    except Exception as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    #return JsonResponse(retorno)
    return render(request, "agregarCategoria.html", retorno)

def listarProducto(request):
    productos = Producto.objects.all()
    retorno = {"productos": productos}
    return render(request, "listarProducto.html", retorno)


def vistaAgregarProducto(request):
    categoria = Categoria.objects.all()
    retorno = {"categoria": categoria}
    return render(request, "agregarProducto.html", retorno)
#consultarProducto

def agregarProducto(request):
    try:
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        precio = request.POST['txtPrecio']
        foto = request.FILES['fileFoto']
        idCategoria = ObjectId(request.POST['cbCategoria'])
        producto = Categoria.objects.get(pk=ObjectId(idCategoria))
        # crear objeto producto
        producto = Producto(proCodigo=codigo,
                            proNombre=nombre,
                            proPrecio=precio,
                            proFoto=foto,
                            proCategoria=producto)
        producto.save()
        mensaje = "Producto agregada correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje, 'idProducto': producto.pk}
    # return JsonResponse(retorno)
    return render(request, "agregarProducto.html", retorno)


def consultarProductoPorId(request, id):
    producto = Producto.objects.get(pk=ObjectId(id))
    categoria = Categoria.objects.all()
    # retornamos los generos porque se necesitan en la interfaz
    retorno = {"producto": producto, "categotia": categoria}
    return render(request, "actualizarProducto.html", retorno)


def actualizarPelicula(request):
    try:
        idProducto = ObjectId(request.POST['idProducto'])
        # obtener la pelicula a partir de su id
        productoActualizar = Producto.objects.get(pk=idProducto)
        # actualizar los campos
        productoActualizar.proCodigo = request.POST['txtCodigo']
        productoActualizar.proNombre = request.POST['txtNombre']
        productoActualizar.proPrecio = request.POST['txtPrecio']
        idCategoria = ObjectId(request.POST['cbCategoria'])
        # obtener el objeto Genero a partir de su id
        categoria = Categoria.objects.get(pk=idCategoria)
        productoActualizar.proCategoria = categoria
        foto = request.FILES.get('fileFoto')

        # si han enviado foto se actualiza el campo
        if (foto):
            # si la pelicula tiene foto debemos eliminarla
            if (productoActualizar.proFoto != ""):
                # primero eliminamos la foto existente
                os.remove(os.path.join(settings.MEDIA_ROOT + "/" +
                                       str(productoActualizar.proFoto)))
            # actualizamos con la nueva foto
            productoActualizar.proFoto = foto

        # actualizar la pelicula en la base de datos
        productoActualizar.save()
        mensaje = "Producto Actualizada"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    # return JsonResponse(retorno)
    return redirect("/listarProducto")


def eliminarProducto(request, id):
    try:
        # buscamos la pelicula por su id
        productoEliminar = Producto.objects.get(pk=ObjectId(id))
        # Eliminamos la pelicula
        productoEliminar.delete()
        mensaje = "Producto Eliminada Correctamente"
    except Error as error:
        mensaje = str(error)
    retorno = {"mensaje": mensaje}
    # return JsonResponse(retorno)
    return redirect('/listarProducto')
