from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('pag1/', views.pag1, name='pag1'),
	path('pag2/', views.pag2, name='pag2'),
	path('about/', views.about, name='about'),
]