from django.shortcuts import render
from django.db.models import Avg,Count
from . models import Product , Category 


# Create your views here.
def index(request):
    categoris =(Category.objects.all().annotate(product_count=Count("product"))
                .prefetch_related("product_set"))
    products= Product.objects.all().order_by("-price").select_related("category") 
    price_avg = Product.objects.aggregate(Avg("price"))["price__avg"]

    context = { 
        "products":products,
        "categories":categoris,
        "price_avg":price_avg,
    }
    return render(request,"products/index.html",context)