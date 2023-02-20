class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self,color):
        posibles=["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in posibles:
            self.color=color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        if type(registro)==int:
            self.registro=registro
        
    def asignarTipo(self,tipo):
        if tipo == ("gasolina" or "electrico"):
            self.tipo=tipo

class Auto:
    cantidad=0
    veracidad=True
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantidadCreados=cantidadCreados

    
    def cantidadAsientos(self):
        for i in range(len(self.asientos)):
            if isinstance(self.asientos[i],Asiento):
                cantidad+=1
        return cantidad
    
    def verificarIntegridad(self):
        if (self.motor.registro==self.registro):
            for i in range(len(self.asientos)):
                if (isinstance(self.asientos[i],Asiento)==False):
                    veracidad=False
        else:
            veracidad=False
        if veracidad==False:
            print("Las piezas no son originales")
        else:
            print("Auto original")

