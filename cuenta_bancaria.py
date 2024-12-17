class SaldoInsuficienteError(Exception):    
    pass

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad) -> float:
        self.saldo += cantidad
    def retirar(self, cantidad) -> float:
        if self.saldo - cantidad < 0:
            raise SaldoInsuficienteError("Error: Fondos insuficientes")
        self.saldo -= cantidad
                 
    def mostrar_saldo(self) -> float:
        return f"Saldo actual: {self.saldo}"   

try:
    cuenta = CuentaBancaria('Juan Pérez', 1000)         
    cuenta.depositar(500)
    cuenta.retirar(200)
    print(cuenta.mostrar_saldo())
    cuenta.retirar(1500)
except SaldoInsuficienteError as error:
    print(f"{error}")    