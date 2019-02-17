from django.shortcuts import render,HttpResponse
from .models import Product

# Create your views here.
def test(request):
    return HttpResponse('HELLO')

def products_list(request):
    products=Product.objects.all()
    print(products)
    return render(request,'products_list.html' ,context={'product_list':products})

def show_product(request, id):
    # p_id=request.GET.get('product_id')
    product=Product.objects.get(id=id)
    return render(request,'show_product.html',context={'product': product})