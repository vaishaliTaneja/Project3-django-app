from django.urls import path
from . import views
from ecomm.settings import DEBUG
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create-product'),
    path('update/<int:product_id>', views.update_product),
    path('delete/<int:product_id>', views.remove_product)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)