from eventos import Evento, Examen,Reuniones,Trabajos_practicos
from Agenda import Agenda
# -*- coding: utf-8 -*-
def Obtener_detalles_evento():
    nombreEvento= input ("ingrese el nombre que le va a dar a su evento: ")
    fecha = input("Ingrese la fecha del evento  ")
    materia = input("Ingrese la materia del evento: ")
    descripcion = input("Ingrese una descripcion del evento: ")
    tipo=input("ingrese el tipo de evento(examen/tp/reunion de estudio)")
    return tipo,nombreEvento,fecha,descripcion, materia
agenda = Agenda()
while True:
  print("1) agregar evento")
  print("2) eliminar evento")
  print("3)mostrar evento")
  print("4) salir")
  opcion= str(input("ingrese una opcion: "))
  if opcion == "1":
            print("--------------------------------------------------------------------------------------")
            tipoE = input("Ingrese el tipo de evento (1)examenes / (2)reuniones / (3)trabajos_practicos): ")
            print("--------------------------------------------------------------------------------------")
            if tipoE== "1":
                tipo,nombreEvento,fecha,descripcion,materia = Obtener_detalles_evento()
                examen = Examen(tipo,nombreEvento,fecha,descripcion,materia)
                agenda.Agregar_evento(examen)
                continue
            if tipoE=="2":
                tipo,nombreEvento,fecha,descripcion,materia = Obtener_detalles_evento()#La línea desempaqueta esta tupla en cuatro variables distintas y 
                examen = Reuniones(tipo,nombreEvento,fecha,descripcion,materia)
                agenda.Agregar_evento(examen)
                continue
            if tipoE=="3":
                tipo,nombreEvento,fecha,descripcion,materia = Obtener_detalles_evento()
                examen = Trabajos_practicos(tipo,nombreEvento,fecha,descripcion,materia)
                agenda.Agregar_evento(examen)
                continue 
        
  if opcion=="2":
      opcion=input("ingrese el nombre del evento")
      agenda.Eliminar_evento(opcion)
      agenda.Mostrar()
      continue              
  if opcion=="3":
      agenda.Mostrar()
      continue
  else:
      exit()  