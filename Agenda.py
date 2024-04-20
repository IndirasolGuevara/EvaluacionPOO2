class Agenda:
  def __init__(self):
        self.eventos = []

  def Agregar_evento(self, evento):
        self.eventos.append(evento)
        if evento in self.eventos:
            print("---------------------------------------")
            print(f"se guardo el evento  correctamente")
            print("---------------------------------------")
        else:
            print("---------------------------------------")
            print("no se guardo")
            print("---------------------------------------")    

  def Mostrar(self):
    if self.eventos:#Verifica si la lista de eventos self.eventos no está vacía.
            print("Lista de eventos:")
            for i, evento in enumerate(self.eventos, start=1):#Itera sobre cada evento en la lista de eventos, utilizando enumerate para obtener tanto el índice i como el objeto evento. El parámetro start=1 indica que queremos que los índices comiencen en 1 en lugar de 0.
                print(f"Evento {i}:")
                print("---------------------------------------")
                print(f"tipo: {evento.tipo.upper()}")
                print(f"nombre: {evento.nombreEvento}")
                print(f"Fecha: {evento.fecha}")
                print(f"Materia: {evento.materia}")
                print(f"Descripción: {evento.descripcion}")
                print("---------------------------------------")
    else:
            print("---------------------------------------")
            print("No hay eventos programados.")
            print("---------------------------------------")

  def Eliminar_evento(self, nombreEvento):
        for evento in self.eventos:
            if nombreEvento == evento.nombreEvento:  
                self.eventos.remove(evento)
                print("-------------------------------------------------------------")
                print(f"Se ha eliminado el evento con la descripción: {nombreEvento}") 
                print("--------------------------------------------------------------")