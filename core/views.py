from django.http import HttpResponse
from django.shortcuts import render

# Create your views here

html_base = """
    <h1>Mi Primer Menu</h1>
    <ul>
        <li>   <a href="/">PORTADA</a>              </li>
        <li>   <a href="/personal/"> personal </a>   </li>
        <li>   <a href="/Notas/"> Notas </a>     </li>
        <li>   <a href="/cursos/"> cursos </a>     </li>
        <li>   <a href="/estudiantes/"> estudiantes </a>  </li>
        <li>   <a href="/asistencia/"> asistencia </a>  </li>
    </ul>
"""

from django.http import HttpResponse
from django.shortcuts import render

html_base = """
    <h1 class="text-center">Dr. Teodoro Maldonado Carbo</h1>
          <li>   <a href="/Notas/"> Notas </a>     </li>
        <li>   <a href="/primer_parcial_primer_quimestre/"> primer_parcial_primer_quimestre </a>   </li>
        <li>   <a href="/segundo_parcial_primer_quimestre/"> segundo_parcial_primer_quimestre </a>     </li>
        <li>   <a href="/tercer_parcial_primer_quimestre/"> tercer_parcial_primer_quimestre </a>     </li>
        <li>   <a href="/evaluacion_primer_quimestre/"> evaluacion_primer_quimestre </a>   </li>
        <li>   <a href="/primer_parcial_segundo_quimestre/"> primer_parcial_segundo_quimestre </a>     </li>
        <li>   <a href="/segundo_parcial_segundo_quimestre/"> segundo_parcial_segundo_quimestre </a>     </li>
         <li>   <a href="/tercer_parcial_segundo_quimestre/"> tercer_parcial_segundo_quimestre </a>   </li>
        <li>   <a href="/evaluacion_segundo_quimestre/"> evaluacion_segundo_quimestre </a>     </li>
        <li>   <a href="/conducta/"> conducta </a>     </li>
        <li>   <a href="/aprovechamiento/"> aprovechamiento </a>     </li>
    
    </ul>
"""


def home(request, template="home.html"):
    return render(request, template);


def Notas(request, template="Notas.html"):
    return render(request, template);



def primer_parcial_primer_quimestre(request, template="primer_parcial_primer_quimestre.html"):
    return render(request, template);


def segundo_parcial_primer_quimestre(request, template="segundo_parcial_primer_quimestre.html"):
    return render(request, template);


def tercer_parcial_primer_quimestre(request, template="tercer_parcial_primer_quimestre.html"):
    return render(request, template);


def evaluacion_primer_quimestre(request, template="evaluacion_primer_quimestre.html"):
    return render(request, template);


def primer_parcial_segundo_quimestre(request, template="primer_parcial_segundo_quimestre.html"):
    return render(request, template);


def segundo_parcial_segundo_quimestre(request, template="segundo_parcial_segundo_quimestre.html"):
    return render(request, template);

def tercer_parcial_segundo_quimestre(request, template="tercer_parcial_segundo_quimestre.html"):
    return render(request, template);


def evaluacion_segundo_quimestre(request, template="evaluacion_segundo_quimestre.html"):
    return render(request, template);

def conducta(request, template="conducta.html"):
    return render(request, template);

def aprovechamiento(request, template="aprovechamiento.html"):
    return render(request, template);

def Consultar(request, template="Consultar.html"):
    return render(request, template);