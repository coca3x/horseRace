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

#new comment..
