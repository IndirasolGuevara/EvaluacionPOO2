
class Evento:
    def __init___(self,tipo,nombreEvento,fecha, descripcion):
        self.tipo = tipo
        self.nombreEvento = nombreEvento
        self.fecha = fecha 
        self.descripcion = descripcion

class Examen(Evento):
    def __init__(self,tipo,nombreEvento, fecha,descripcion,materia):
        super().__init__()
        self.tipo = tipo
        self.nombreEvento = nombreEvento
        self.fecha = fecha
        self.descripcion = descripcion
        self.materia = materia
        
    def __str__(self):
        return f"Materia: {self.materia}, para el dia: {self.fecha}  Descripcion: {self.descripcion}"    


class Trabajos_practicos(Evento):
    def __init__(self,tipo,nombreEvento, fecha,descripcion,materia):#lo tuve que poner de esta forma porque con super no me tomaba mas de un elemento
        super().__init__()
        self.tipo = tipo
        self.nombreEvento = nombreEvento
        self.fecha = fecha
        self.descripcion = descripcion
        self.materia = materia
        
    def __str__(self):
        return f"Materia: {self.materia}, para el dia: {self.fecha}  Descripcion: {self.descripcion}"
    

class Reuniones(Evento):
    def __init__(self,tipo,nombreEvento, fecha,descripcion,materia):
        super().__init__()
        self.tipo=tipo
        self.nombreEvento = nombreEvento
        self.fecha = fecha
        self.descripcion = descripcion
        self.materia = materia
        
    def __str__(self):
        return f"Materia: {self.materia}, para el dia: {self.fecha}  Descripcion: {self.descripcion}"