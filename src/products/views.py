from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def product_detail_form(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, "products/product_create.html", context)
    #return render(request, "home.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }

    return render(request, "products/product_details.html", context)
    #return render(request, "home.html", context)