
# Horse Racing Game

This script simulates a horse race between multiple players. Each player controls a horse that advances randomly along a 50-unit track. The first to reach the finish line wins the race.

## Requirements

- Python 3.x
- Windows, macOS, or Linux operating system

## Installation

1. Clone this repository to your local machine:
   ```sh
   git clone <REPOSITORY_URL>
   ```

2. Navigate to the project directory:
   ```sh
   cd <DIRECTORY_NAME>
   ```

## Usage

1. Run the script:
   ```sh
   python horse_race.py
   ```

2. Enter the number of players when prompted. Each player will control a horse in the race.

## Code Description

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
        print(f"Player {i+1}: {track[:finish_line + 1]}")
    print("Finish Line: " + '-' * finish_line)

def horse_race(num_players):
    horses = [0] * num_players
    finish_line = 50
    while True:
        print_race(horses, finish_line)
        if max(horses) >= finish_line:
            winner = horses.index(max(horses)) + 1
            print(f"Player {winner} has won the race!")
            break
        for i in range(num_players):
            horses[i] += random.randint(1, 5)
        time.sleep(0.5)

num_players = int(input("Enter the number of players: "))
horse_race(num_players)
```

### Functions

- `clear_console()`: Clears the console to keep the race interface updated.
- `print_race(horses, finish_line)`: Prints the current position of each horse in the race.
- `horse_race(num_players)`: Controls the main logic of the race, including the random advancement of the horses and detection of the winner.

## Notes

- The script uses special characters to represent the horses on the track. Make sure your console supports these characters for proper visualization.
- The race progresses in half-second intervals (`time.sleep(0.5)`), giving it a real-time feel.

## Contributions

Contributions are welcome. If you find any issues or have any improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
