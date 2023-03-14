import base64
from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductCreate
from django.http import HttpResponse
from base64 import b64encode

def index(request):
    shelf = Products.objects.all()
    products = []
    for product in shelf:
        temp = {
            "productid": product.productid,
            "price": product.price,
            "productname": product.productname,
            "productdec" : product.productdec,
            "quantity": product.quantity
        }
        products.append(temp)
    return render(request, 'list.html', {'shelf': products})

def remove_product(request, product_id):
    product_id = int(product_id)
    product = Products.objects.get(productid = product_id)
    product.delete()
    return redirect('index')

def create(request):
    product = ProductCreate()
    if request.method == 'POST':
        product = ProductCreate(request.POST, request.FILES)
        if product.is_valid():
            product.save()
            return redirect('index')
        else:
            return HttpResponse("""Data provided is not valid, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'update_create.html', {'product':product})

def update_product(request, product_id):
    product_id = int(product_id)
    try:
        product = Products.objects.get(productid = product_id)
    except Products.DoesNotExist:
        return redirect('index')
    productDetails = ProductCreate(request.POST or None, instance = product)
    if productDetails.is_valid():
       productDetails.save()
       return redirect('index')
    return render(request, 'update_create.html', {'product':productDetails})