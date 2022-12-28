import random
import time
import os

field_area = [
    "⬛" * 25,
    "⬛" * 25,
    "⬛" * 25,
    "⬛" * 25,
    "⬛" * 25,
    "⬛" * 25,
    "⬜" * 25
]



player = {
    "x": 5,
    "y": 0,
    "hp": 3
}

bombs = []
for i in range(50):
    x = random.randint(1, 24)
    y = random.randint(1, 5)
    bombs.append((y, x, False))

restart_game = True

while restart_game:
    for y, row in enumerate(field_area):
        for x, cell in enumerate(row):
            if player["x"] == x and player["y"] == y:
                print("🧍", end=" ")
            if (y, x, True) in bombs:
                print("💣", end=" ")
            else:
                print(cell, end=" ")
        print()
    y, x = player["y"], player["x"]
    if (y, x) in [(b[0], b[1]) for b in bombs]:
        if player["hp"] > 0:
            player["hp"] = player["hp"] - 1
            print("\n" * 10)
            print("You touch the bomb")
            print("\n" * 2)
            print("you have currently have " + str(player["hp"]) + " HP")
            print("\n" * 2)
            time.sleep(2)
            bombs = [(y, x, True) if (y, x) == (b[0], b[1]) else b for b in bombs]
            for y, row in enumerate(field_area):
                for x, cell in enumerate(row):
                    if player["x"] == x and player["y"] == y:
                        print("🧍", end=" ")
                    elif (y, x) in bombs:
                        print("⬛", end=" ")
                    else:
                        print(cell, end=" ")
                print()

    move = input("Enter a move (a/s/d): ")
    if move == "a" and player["x"] > 0:
        print("\n" * 10)
        player["x"] -= 1
    elif move == "s" and player["y"] < 6:
        print("\n" * 10)
        player["y"] += 1
    elif move == "d" and player["x"] < 24:
        print("\n" * 10)
        player["x"] += 1

    if player["hp"] <= 0:
        print("Game over! You have died.")
        print("you have " + str(player["hp"]))
        restart = input("would you like to play again? (y/n)")

        if restart == "y":
            player["hp"] = 3
            player["x"] = 5
            player["y"] = 0
            bombs = []
            for i in range(50):
                x = random.randint(1, 24)
                y = random.randint(1, 5)
                bombs.append((y, x))
                if player["x"] == x and player["y"] == y:
                    print("🧍", end=" ")

        if restart == "n":
            player["hp"] = 3
            player["x"] = 5
            player["y"] = 0
            restart_game = False
            break
    if player["y"] == 6:
        print("Congratulations! You have reached the finished line.")
        time.sleep(2)
        restart = input("would you like to play again? (y/n)")
        if restart == "y":
            player["hp"] = 3
            player["x"] = 5
            player["y"] = 0
            bombs = []
            for i in range(50):
                x = random.randint(1, 24)
                y = random.randint(1, 5)
                bombs.append((y, x))
                if player["x"] == x and player["y"] == y:
                    print("🧍", end=" ")

        if restart == "n":
            player["hp"] = 3
            player["x"] = 5
            player["y"] = 0
            restart_game = False
            break
print("\n" * 10)
print("Thank you for playing!")
print("\n" * 5)