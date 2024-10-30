from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Empleado:
    codigo: int
    nombre: str
    puesto: str
    profesion: str

@dataclass
class Salario:
    codigo_empleado: int
    numero_pago: int
    fecha_pago: str
    sueldo_base: float
    bonificacion: float
    sueldo_bruto: float = 0.0
    igss: float = 0.0
    sueldo_neto: float = 0.0


empleados: List[Empleado] = []
salarios: List[Salario] = []

def configurar_empleados(cantidad: int):
    print(f"Capacidad configurada para {cantidad} empleados.")

def registrar_empleado():
    codigo = int(input("Ingrese el código del empleado: "))
    nombre = input("Ingrese el nombre del empleado: ")
    puesto = input("Ingrese el puesto del empleado: ")
    profesion = input("Ingrese la profesión del empleado: ")
    
    empleado = Empleado(codigo, nombre, puesto, profesion)
    empleados.append(empleado)
    print("Empleado registrado correctamente.")

def buscar_empleado(codigo: int) -> Optional[Empleado]:
    for emp in empleados:
        if emp.codigo == codigo:
            return emp
    return None

def registrar_salario():
    codigo = int(input("Ingrese el código del empleado: "))
    empleado = buscar_empleado(codigo)
    
    if empleado:
        numero_pago = int(input("Ingrese el número de pago: "))
        fecha_pago = input("Ingrese la fecha de pago: ")
        sueldo_base = float(input("Ingrese el sueldo base: "))
        bonificacion = float(input("Ingrese la bonificación: "))
       # no se si esta bien pero para calcular el iggs
    
        sueldo_bruto = sueldo_base + bonificacion
        igss = sueldo_bruto * 0.0483
        sueldo_neto = sueldo_bruto - igss
        
        salario = Salario(codigo, numero_pago, fecha_pago, sueldo_base, bonificacion, sueldo_bruto, igss, sueldo_neto)
        salarios.append(salario)
        print(f"Salario registrado para {empleado.nombre}.")
    else:
        print("Empleado no encontrado. Intente de nuevo.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Configuración de Empleados")
        print("2. Registro de Empleados")
        print("3. Registro de Salarios")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            cantidad = int(input("Ingrese la cantidad de empleados: "))
            configurar_empleados(cantidad)
        elif opcion == '2':
            registrar_empleado()
        elif opcion == '3':
            registrar_salario()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


menu()
