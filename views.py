from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from core.forms import ProductForm
from core.models import Product
from core.models import Brand
from core.forms import BrandForm
from core.models import Supplier
from core.forms import SupplierForm
from .models import Category
from .forms import CategoryForm

# Create your views here.

def home(request):
   data = {
        "title1":"Autor | StudentCode",
        "title2":"Super Mercado Economico"
   }
   return render(request,'core/home.html',data)

  #  return HttpResponse(f"<h1>{data['title2']}<h1>\
  #                        <h2>Le da la Bienvenida  a su selecta clientela</h2>")
  #  products = ["aceite","coca cola","embutido"]
  #  prods_obj=[{'nombre': producto} for producto in products] # json.dumps()
  #  return JsonResponse({'mensaje2': data,'productos':prods_obj})

 
  #  return HttpResponse(f"<h1>{data['title2']}<h1>\
  #                      <h2>Le da la Bienvenida  a su selecta clientela</h2>")
# vistas de productos: Listar productos 
def product_List(request):
    data = {
        "title1": "Productos",
        "title2": "Consulta De Productos"
    }
    products = Product.objects.all() # select * from Product
    data["products"]=products
    return render(request,"core/products/list.html",data)
# crear un producto
def product_create(request):
    data = {"title1": "Productos","title2": "Ingreso De Productos"}
   
    if request.method == "POST":
        #print(request.POST)
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("core:product_list")

    else:
        data["form"] = ProductForm() # controles formulario sin datos

    return render(request, "core/products/form.html", data)

# editar un producto
def product_update(request,id):
    data = {"title1": "Productos","title2": "Edicion De Productos"}
    product = Product.objects.get(pk=id)
    if request.method == "POST":
      form = ProductForm(request.POST,request.FILES, instance=product)
      if form.is_valid():
            form.save()
            return redirect("core:product_list")
    else:
        form = ProductForm(instance=product)
        data["form"]=form
    return render(request, "core/products/form.html", data)


# eliminar un producto
def product_delete(request,id):
    product = Product.objects.get(pk=id)
    data = {"title1":"Eliminar","title2":"Eliminar Un Producto","product":product}
    if request.method == "POST":
        product.delete()
        return redirect("core:product_list")
 
    return render(request, "core/products/delete.html", data)

# vistas de marcas: Listar marcas
# Lista de marcas
def brand_List(request):
    data = {
        "title1": "Marcas",
        "title2": "Consulta De Marcas"
    }
    brands = Brand.objects.all()  # select * from Brand
    data["brands"] = brands
    return render(request, "core/brands/list.html", data)

# Crear una marca
def brand_create(request):
    data = {"title1": "Marcas", "title2": "Ingreso De Marcas"}
   
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            brand.save()
            return redirect("core:brand_list")
    else:
        data["form"] = BrandForm()  # controles formulario sin datos

    return render(request, "core/brands/form.html", data)

# Editar una marca
def brand_update(request, id):
    data = {"title1": "Marcas", "title2": "Edición De Marcas"}
    brand = Brand.objects.get(pk=id)
    if request.method == "POST":
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect("core:brand_list")
    else:
        form = BrandForm(instance=brand)
        data["form"] = form
    return render(request, "core/brands/form.html", data)

# Eliminar una marca
def brand_delete(request, id):
    brand = Brand.objects.get(pk=id)
    data = {"title1": "Eliminar", "title2": "Eliminar Una Marca", "brand": brand}
    if request.method == "POST":
        brand.delete()
        return redirect("core:brand_list")
    return render(request, "core/brands/delete.html", data)

# vistas de proveedores: Listar proveedores
from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm

# Lista de proveedores
def supplier_List(request):
    data = {
        "title1": "Proveedores",
        "title2": "Consulta de Proveedores"
    }
    suppliers = Supplier.objects.all()
    return render(request, "core/suppliers/list.html", {'suppliers': suppliers, **data})

# Crear un proveedor
def supplier_create(request):
    data = {
        "title1": "Proveedores",
        "title2": "Crear Proveedor"
    }
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'core/suppliers/create.html', {'form': form, **data})

# Editar un proveedor
def supplier_update(request, id):
    data = {
        "title1": "Proveedores",
        "title2": "Editar Proveedor"
    }
    supplier = Supplier.objects.get(id=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('core:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'core/suppliers/edit.html', {'form': form, 'supplier': supplier, **data})

# Eliminar un proveedor
def supplier_delete(request, id):
    data = {
        "title1": "Proveedores",
        "title2": "Eliminar Proveedor"
    }
    supplier = Supplier.objects.get(id=id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('core:supplier_list')
    return render(request, 'core/suppliers/delete.html', {'supplier': supplier, **data})

# vistas de categorías: Listar categorias
# Lista de categorías
def category_List(request):
    data = {
        "title1": "Categorías",
        "title2": "Consulta De Categorías"
    }
    categories = Category.objects.all()
    data["categories"] = categories
    return render(request, "core/categories/list.html", data)

# Crear una categoría
def category_create(request):
    data = {"title1": "Categorías", "title2": "Ingreso De Categorías"}
   
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("core:category_list")
    else:
        data["form"] = CategoryForm()

    return render(request, "core/categories/form.html", data)

# Editar una categoría
def category_update(request, id):
    data = {"title1": "Categorías", "title2": "Edición De Categorías"}
    category = Category.objects.get(pk=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("core:category_list")
    else:
        form = CategoryForm(instance=category)
        data["form"] = form
    return render(request, "core/categories/form.html", data)

# Eliminar una categoría
def category_delete(request, id):
    category = Category.objects.get(pk=id)
    data = {"title1": "Eliminar", "title2": "Eliminar Una Categoría", "category": category}
    if request.method == "POST":
        category.delete()
        return redirect("core:category_list")
    return render(request, "core/categories/delete.html", data)



  