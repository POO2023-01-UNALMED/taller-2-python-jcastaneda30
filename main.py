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
        if tipo == "gasolina" or tipo=="electrico":
            self.tipo=tipo

class Auto:
    cantidadCreados=0
    veracidad=True
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    
    def cantidadAsientos(self):
        cantidad=0
        for i in range(len(self.asientos)):
            if isinstance(self.asientos[i],Asiento):
                cantidad+=1
        return cantidad
    
    def verificarIntegridad(self):
        if (self.motor.self.registro==self.registro):
            for i in range(len(self.asientos)):
                if (self.asientos.self.registro[i]!=self.registro):
                    veracidad=False
        else:
            veracidad=False
        if veracidad==False:
            return "Las piezas no son originales"
        else:
            return "Auto original"

