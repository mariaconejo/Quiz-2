class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("======================")
        print("El juego ha comenzado..")
        print("======================")
        print(f"Aqui va el juego o los metodos de instancia donde vas a crear la logica del juego.")
        self.cifrado(self.nombre_jugador) # Se llaman a los metodos donde esta logica de los juegos
        self.bubble(self.nombre_jugador)
        print("¡Gracias por jugar!\n")

    def salir(self):
        print("======================")
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")

    # Para este ejercicio use codigo ASCII
    def cifrado(self, nombre):
        print("======================")
        print(f"!Bienvenido al juego del cifrado!, {nombre}") # Se le da la bienvenida al usuario al juego del cifrado
        print("======================")
        texto = input("Por favor, ingrese el texto a cifrar: ") # Pedir el texto al usuario
        desplazamiento = 1 # Se va desplazar una letra a la derecha, se puede modificar para se mueva dos o 3 o lo que el  usuario quiera
        resultado = ""

        for caracter in texto: # Recorrer cada caracter del texto ingresado
            if caracter.isalpha():  # Ignora caracteres no alfabeticos
                letra_cifrada = chr(((ord(caracter.upper()) - ord('A') + desplazamiento) % 26) + ord('A')) # Conversion de numeros a codigo ASCII y viceversa conr ord y chr
                """ Convertir el texto ingresado a mayusculas, porque el codigo ASCII de letras mayusculas y minisculas es diferente
                    ord(caracter.upper()) - ord('A') hace una resta, para encontrar la posicion de la letra en el alfabeto
                    para este ejercicio estoy usando el codigo ASCII, por ejemplo H es 72 y A es 65, entonces 72 - 65 = 7 a esto
                    se le agrega el dezplamiento, siguiendo con el ejemplo 7+1 = 8, luego el % 26 me asegura que el resultado sigue estando 
                    dentro del rango del alfabeto y en caso de llegar a Z , comience nuevamente en A
                    + ord('A') Finalmente le suma el valor de A en codigo ASCII que es 65 + 8 = 73 donde 73 es el codigo ASCII de la I """
                    
                resultado += letra_cifrada
            else:
                resultado += caracter  # Ignora los caracteres no alfabeticos

        print("Texto cifrado:", resultado)
        print(f"¡Felicidades {nombre} tu texto se ha cifrado!")
        print("======================")
        
    def bubble(self, nombre):
        print(f"!Bienvenido al juego de la burbuja!, {nombre}")  # Se le da la bienvenida al usuario al juego de las burbujas
        # Pedir al usuario que ingrese los números separados por espacios
        entrada = input("Por favor, ingrese unicamente números separados por espacios: ") # Me retorna una cadena de esta forma ["1 2 3 4"]

        # Convertir la entrada en una lista de números
        numeros = [] 
        for i in entrada.split():
            numeros.append(int(i))
        """ Se debe convertir porque el usuario al digitar con espacios el int(input()) da error porque no puede convertir una cadena
            con espacios o comas, el for separa cada elemento en partes, y el int convierte cada elemento en un numero entero
            lo que me convierte la cadena inicial a esto ["1", "2", "3", "4"] y luego lo agrega a la lista de numeros[]"""

        # Bubble con for aninado sin usar el metodo sort
        for i in range(len(numeros)): # Me dice cuantas veces se debe ejecutar, dependiendo del tamaño de mi lista por eso use len y range
            for j in range(len(numeros) - 1): # Recorre la lista para hacer la comparacion dentro de la lista y ordenarla el -1 es para evitar que se salga del limite cuand compare el ultimo valor
                if numeros[j] > numeros[j + 1]: # Verificar Si el numero actual es mayor que el siguiente 
                    temp = numeros[j] # Guarda el valor original del numero
                    numeros[j] = numeros[j + 1] # Sobreescribe el numero al hacer la comparacion
                    numeros[j + 1] = temp  # Se intercambian y el mayor se mueve a la derecha  
                    # uso variable temporal para almacenar valores de forma transitoria y asi poder hacer la comparacion
        # Mostrar la lista ordenada
        print("Lista ordenada:", numeros)
        print(f"¡Felicidades {nombre} tu lista se ha ordenado!")
    
""" Referencias   
    Pdf del profesor
    https://parzibyte.me/blog/2018/12/10/ord-chr-python/
    https://www.picuino.com/es/python-for-anidados.html
    https://www.w3schools.com/python/ref_string_isalpha.asp
    https://www.ionos.com/es-us/digitalguide/paginas-web/desarrollo-web/python-split/
    https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3-es
    https://ellibrodepython.com/range-python
    https://en.wikipedia.org/wiki/Temporary_variable#:~:text=In%20computer%20programming%2C%20a%20temporary,a%20variable%20with%20local%20scope."""

    


