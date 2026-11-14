from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404

# Create your views here.
def store(request):
    
    all_Products = Product.objects.all()
    context = {"my_products": all_Products}
    
    return render(request, "store/store.html", context=context)

def categories(request):
    all_categories = Category.objects.all()
    return {"all_categories": all_categories}

def product_info(request, slug):
    
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    
    return render(request, "product-info.html", context=context)