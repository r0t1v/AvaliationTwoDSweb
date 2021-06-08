from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('pag1/', views.pag1, name='pag1'),
	path('pag2/', views.pag2, name='pag2'),
	path('pag3/', views.pag3, name='pag3'),
	path('pag4/', views.pag4, name='pag4'),
	path('pag5/', views.pag5, name='pag5'),
	path('pag6/', views.pag6, name='pag6'),
	path('pag7/', views.pag7, name='pag7'),
	path('pag8/', views.pag8, name='pag8'),
	path('pag9/', views.pag9, name='pag9'),
	path('pag10/', views.pag10, name='pag10'),
	path('about/', views.about, name='about'),
]