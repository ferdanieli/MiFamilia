from _datetime import date
from django.shortcuts import render

from django.http import HttpResponse
from AppFamilia.models import Familia

def ingresar_miembro(request):

    contexto = {
        "miembros": [
            {
                "Nombre de mi mamá": "Cris",
                "Apellido": "Polli",
                "Edad": 72,
                "Fecha de nacimiento": date(1951, 10, 4)

            },
            {
                "Nombre de mi hermana mayor": "Naty",
                "Apellido": "Polli",
                "Edad": 48,
                "Fecha de nacimiento": date(1975,3,4),
            },
            {
                "Nombre de mi hermana melliza": "Sole",
                "Apellido": "Polli",
                "Edad": 45,
                "Fecha de nacimiento": date(1978,8,2),
            },
            {
                "Yo soy": "Fer",
                "Apellido": "Polli",
                "Edad": 45,
                "Fecha de nacimiento": date(1978,8,2)
            },
        ]
    }
    return render(request, "template.html", contexto)