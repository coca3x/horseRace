
# Carrera de Caballos

Este script simula una carrera de caballos entre varios jugadores. Cada jugador tiene un caballo que avanza aleatoriamente a lo largo de una pista de 50 unidades. El primero en llegar a la meta gana la carrera.

## Requisitos

- Python 3.x
- Sistema operativo Windows, macOS o Linux

## Instalación

1. Clona este repositorio en tu máquina local:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   ```

2. Navega al directorio del proyecto:
   ```sh
   cd <NOMBRE_DEL_DIRECTORIO>
   ```

## Uso

1. Ejecuta el script:
   ```sh
   python horse_race.py
   ```

2. Introduce el número de jugadores cuando se te solicite. Cada jugador controlará un caballo en la carrera.

## Descripción del Código

```python
import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_race(horses, finish_line):
    clear_console()
    for i, horse in enumerate(horses):
        track = '-' * horse + '🐎' + '-' * (finish_line - horse)
        print(f"Jugador {i+1}: {track[:finish_line + 1]}")
    print("Meta: " + '-' * finish_line)

def horse_race(num_players):
    horses = [0] * num_players
    finish_line = 50
    while True:
        print_race(horses, finish_line)
        if max(horses) >= finish_line:
            winner = horses.index(max(horses)) + 1
            print(f"¡El jugador {winner} ha ganado la carrera!")
            break
        for i in range(num_players):
            horses[i] += random.randint(1, 5)
        time.sleep(0.5)

num_players = int(input("Introduce el número de jugadores: "))
horse_race(num_players)
```

### Funciones

- `clear_console()`: Limpia la consola para mantener la interfaz de la carrera actualizada.
- `print_race(horses, finish_line)`: Imprime la posición actual de cada caballo en la carrera.
- `horse_race(num_players)`: Controla la lógica principal de la carrera, incluyendo el avance aleatorio de los caballos y la detección del ganador.

## Notas

- El script usa caracteres especiales para representar a los caballos en la pista. Asegúrate de que tu consola soporte estos caracteres para una visualización adecuada.
- La carrera avanza en intervalos de medio segundo (`time.sleep(0.5)`), lo que le da una sensación de tiempo real.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
