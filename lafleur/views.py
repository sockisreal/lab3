from rest_framework import viewsets
from lafleur.serializers import *
from lafleur.models import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("product_name")
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
