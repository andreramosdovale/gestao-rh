from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [
    path('create', EmpresaCreate.as_view(), name='create_empresa'),
    path('edit/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),
]
