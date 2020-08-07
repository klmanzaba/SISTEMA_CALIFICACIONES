from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('Notas/', views.Notas, name="Notas"),
    path('primer_parcial_primer_quimestre/', views.primer_parcial_primer_quimestre, name="primer_parcial_primer_quimestre"),
    path('segundo_parcial_primer_quimestre/', views.segundo_parcial_primer_quimestre, name="segundo_parcial_primer_quimestre"),
    path('tercer_parcial_primer_quimestre/', views.tercer_parcial_primer_quimestre, name="tercer_parcial_primer_quimestre"),
    path('Evaluacion_primer_quimestre/', views.evaluacion_primer_quimestre, name="evaluacion_primer_quimestre"),
    path('primer_parcial_segundo_quimestre/', views.primer_parcial_segundo_quimestre, name="primer_parcial_segundo_quimestre"),
    path('segundo_parcial_segundo_quimestre/', views.segundo_parcial_segundo_quimestre, name="segundo_parcial_segundo_quimestre"),
    path('tercer_parcial_segundo_quimestre/', views.tercer_parcial_segundo_quimestre, name="tercer_parcial_segundo_quimestre"),
    path('Evaluacion_segundo_quimestre/', views.evaluacion_segundo_quimestre, name="evaluacion_segundo_quimestre"),
    path('Conducta/', views.conducta, name="conducta"),
    path('Aprovechamiento/', views.aprovechamiento, name="aprovechamiento"),
    path('Consultar/', views.Consultar, name="Consultar"),
    path('admin/', admin.site.urls),
]