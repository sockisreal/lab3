from django.contrib import admin
from lafleur import views as lafleur_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', lafleur_views.ProductViewSet)
router.register(r'category', lafleur_views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
