import math

distancias = {
    "Santiago": {"Buenos Aires": 1400},
    "Valparaiso": {"Buenos Aires": 1450},
    "Concepcion": {"Buenos Aires": 1200},
}

duraciones = {
    "Auto": 12,
    "Bus": 18,
    "Avión": 2,
}

def calcular_distancia(ciudad_origen, ciudad_destino):
    return distancias.get(ciudad_origen, {}).get(ciudad_destino)

def mostrar_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, medio_transporte):
    print(f"\nInicias tu viaje desde {ciudad_origen} hacia {ciudad_destino}.")
    print(f"La distancia es de {distancia} km, que son aproximadamente {distancia * 0.621371} millas.")
    print(f"El tiempo estimado de viaje es de {duracion} horas en {medio_transporte}.")

while True:
    ciudad_origen = input("Ingrese la Ciudad de Origen (Santiago, Valparaíso, Concepción): ")
    ciudad_destino = input("Ingrese la Ciudad de Destino (Buenos Aires): ")

    distancia = calcular_distancia(ciudad_origen, ciudad_destino)

    if distancia:
        medio_transporte = input("Seleccione el medio de transporte (Auto, Bus, Avión): ")
        duracion = duraciones.get(medio_transporte)

        if duracion:
            mostrar_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, medio_transporte)
        else:
            print("Medio de transporte no válido.")
    else:
        print("No se encontró la distancia entre las ciudades.")

    salir = input("¿Desea salir? (s para salir): ")
    if salir.lower() == 's':
        break
