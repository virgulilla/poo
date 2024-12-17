from math import pi

class Circulo:
    def __init__(self, radio: float = 0.0):
        self.radio = radio

    def calcularArea(self) -> float:
        return pi * self.radio ** 2
    def calcularPerimetro(self) -> float:
        return 2 * pi * self.radio

circulo = Circulo(5)
print("Area: ",circulo.calcularArea())
print("Perimetro: ",circulo.calcularPerimetro())