from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('funcionario/', include('apps.funcionarios.urls')),
    path('account/', include('django.contrib.auth.urls')),
    # path('departamento/', include('apps.departamento.urls')),
    path('empresa/', include('apps.empresas.urls')),
    # path('registro_hora_extra/', include('apps.registro_hora_extra.urls')),
]
