from django.urls import path


urlpatterns = [
    path('producto/','views.mostrar_productos',name='producto')
]