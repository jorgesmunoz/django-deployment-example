from django.urls import path, include
from basic_app import views

# Template tagging (Django looks for this variable)
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
