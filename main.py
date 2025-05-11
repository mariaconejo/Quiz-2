from Juego import Juego

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego")
    print("2. Salir")


def main():
    nombre = input("Ingresa tu nombre para comenzar: ")
    juego = Juego(nombre)
    valor=True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            juego.iniciar_juego()
        elif opcion == "2":
            juego.salir()
            valor=False
        else:
            print("Opción inválida. Intenta de nuevo.\n")

main()

"""
  MEJORAS
  Se puede mejorar en que ambos programas sean mas optimos en especial el de bubble,
  El de cifrado me intereso mucho y se puede pedirle al usuario que escoga el desplazamiento y agregar simbolos y numeros
  El cifrado permita criptar y desencriptar
  El de bubble que acepte numeros float,
  Elegir si el usuario quiere ordenar los numeros de forma ascendente o descendente
"""
  
