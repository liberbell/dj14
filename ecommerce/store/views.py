from django.shortcuts import render
from . models import Category, Product

# Create your views here.
def store(request):
    
    all_Products = Product.objects.all()
    context = {"my_products": all_Products}
    
    return render(request, "store/store.html", context=context)

def categories(request):
    all_categories = Category.objects.all()
    return {"all_categories": all_categories}