import random
from time import sleep

from clases.jugador import Jugador
from clases.carta import Carta

def crear_mazo():
        valores = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]
        palos = ["espada", "basto", "oro", "copa"]

        mazo = [Carta(valor, palo) for palo in palos for valor in valores]
        random.shuffle(mazo)

        return mazo
    
def valor_carta(carta: Carta) -> int:

    jerarquia = {
        ("1", "espada"): 14,
        ("1", "basto"): 13,
        ("7", "espada"): 12,
        ("7", "oro"): 11,
        ("3", None): 10,
        ("2", None): 9,
        ("1", None): 8,
        ("12", None): 7,
        ("11", None): 6,
        ("10", None): 5,
        ("7", None): 4,
        ("6", None): 3,
        ("5", None): 2,
        ("4", None): 1,
    }

    clave_especifica = (carta.valor, carta.palo)

    clave_general = (carta.valor, None)

    return jerarquia.get(clave_especifica, jerarquia.get(clave_general, 0))
        
    


def comparar_cartas(carta1: Carta, carta2: Carta):
    valor1 = valor_carta(carta1)
    valor2 = valor_carta(carta2)

    print(f"DEBUG: {carta1} tiene valor {valor1}, {carta2} tiene valor {valor2}")

    if valor1 > valor2:
        print(f"{carta1} gana la ronda.")
        return carta1  
    elif valor2 > valor1:
        print(f"{carta2} gana la ronda.")
        return carta2  
    else:
        print("Empate.")
        return None  
    
def mostrar_estado(jugador1: Jugador, jugador2: Jugador):
    print(f"\nPuntos {jugador1.nombre}: {jugador1.puntos} | Puntos {jugador2.nombre}: {jugador2.puntos}")
    print("")
    print(f"{jugador1.nombre} mano: {jugador1.mostrar_mano()}")
    print(f"{jugador2.nombre} mano: {jugador2.mostrar_mano()}")

def jugar_truco(nombre_jugador: str):
    mazo = crear_mazo()
    jugador1 = Jugador(nombre_jugador)
    jugador2 = Jugador("Jugador 2")

    jugador1.recibir_cartas(mazo[0:3])
    jugador2.recibir_cartas(mazo[3:6])

    print(jugador1.mostrar_mano())

    numero_carta_max = 3
    ronda = 0
    numero_jugada = 0
    truco_cantado = False
    truco_denegado = False

    while ronda < 3:
        
       
        respuesta_truco = ("si", "no")
        
        print(f"\n--- Ronda {numero_jugada + 1} ---")
        numero_jugada += 1
        print("1. Jugar carta")

        if truco_denegado == False:
            if truco_cantado == False:
                print("2. Truco")
            else:
                print("2. Retruco")

        print("3. Retirarse")

        opcion_a_jugar = int(input("Ingrese su jugada: "))
        while truco_denegado == True and opcion_a_jugar == 2:
            opcion_a_jugar = int(input("Ingrese una opcion valida: "))


        match opcion_a_jugar:

            case 1:
                seleccion_carta = int(input(f"Ingrese la carta que quiere jugar: (1 , {numero_carta_max}) "))
                while seleccion_carta > len(jugador1.mano) :
                    seleccion_carta = int(input(f"Ingrese un numero entre 1 y {numero_carta_max}: "))

                numero_carta_max -= 1

                carta1 = jugador1.mano.pop(seleccion_carta - 1)
                
                print("\n. . .")
                sleep(1)
                
                carta2 = jugador2.mano.pop(0)

                print(f"\n{jugador1.nombre} juega: {carta1}")
                
                print(f"\n{jugador2.nombre} juega: {carta2}")
                
                ganador = comparar_cartas(carta1, carta2)

                punto_a_ganar = 1

                if truco_denegado == False:
                    if respuesta_truco == "si":
                        punto_a_ganar = 2   
                    elif respuesta_truco == "si" and truco_cantado == True:
                        punto_a_ganar = 3

                if ganador == carta1:
                    print(f"\n{jugador1.nombre} gana esta ronda!")
                    jugador1.ganar_punto(punto_a_ganar)
                elif ganador == carta2:
                    print(f"\n{jugador2.nombre} gana esta ronda!")
                    jugador2.ganar_punto(punto_a_ganar)
                else:
                    print("\nEmpate esta ronda.")

                ronda += 1

            case 2:
                if truco_denegado == False:
                    respuesta = random.choice(respuesta_truco)
                    if respuesta == "si":
                        truco_cantado = True
                    else:
                        truco_denegado = True
                    print(respuesta)

                if truco_cantado == True and respuesta == "no":
                    jugador1.ganar_punto(3)
                

            case 3:
                jugador2.ganar_punto(3)
                ronda = 3
                
        mostrar_estado(jugador1, jugador2)
       
    if jugador1.puntos > jugador2.puntos:
        print(f"\n¡El Ganador es {jugador1.nombre}!")
    elif jugador2.puntos > jugador1.puntos:
        print("\n¡El Ganador es Jugador 2!")
    else:
        print("\n¡Es un empate!")
    
    
    



