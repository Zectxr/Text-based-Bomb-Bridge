import random
import time

#
field_area = ["⬛" * 50 for i in range(20)] + [("⬛"+"⬜")*(25)] + [("⬜"+"⬛")*(25)]



# initialize player character x coordinate and y coordinate and player health points
player = {
    "x": 25,
    "y": 0,
    "hp": 3
}

# value of how many do you want to be placed

difficulty = 500

# create 50 invisible bombs at random locations

bombs = []
for i in range(difficulty):
    x = random.randint(0, 50)
    y = random.randint(1, 19)
    bombs.append((y, x, True)) # Invisible or Visible bomb: True & False

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

        # check if player has stepped on a bomb

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

            # remove the bomb that the player stepped on

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

    # get player's input for movement

    move = input("Enter a move (a/s/d): ")
    if move == "a" and player["x"] > 0:
        print("\n" * 10)
        player["x"] -= 1
    elif move == "s" and player["y"] < 20:
        print("\n" * 10)
        player["y"] += 1
    elif move == "d" and player["x"] < 49:
        print("\n" * 10)
        player["x"] += 1

    # check if player has run out of health points

    if player["hp"] <= 0:
        print("Game over! You have died.")
        print("you have " + str(player["hp"]))
        restart = input("would you like to play again? (y/n)")

        if restart == "y":
            player["hp"] = 3
            player["x"] = 25
            player["y"] = 0
            bombs = []
            for i in range(difficulty):  # difficulty
                x = random.randint(0, 50)
                y = random.randint(1, 19)
                bombs.append((y, x))
                if player["x"] == x and player["y"] == y:
                    print("🧍", end=" ")

        if restart == "n":
            player["hp"] = 3
            player["x"] = 5
            player["y"] = 0
            restart_game = False
            break

            # check if player has reached the finish line

    if player["y"] == 20:
        print("Congratulations! You have reached the finished line.")
        time.sleep(2)
        restart = input("would you like to play again? (y/n)")
        if restart == "y":
            player["hp"] = 3
            player["x"] = 5
            player["y"] = 0
            bombs = []
            for i in range(difficulty):  # difficulty
                x = random.randint(1, 50)
                y = random.randint(1, 19)
                bombs.append((y, x))
                if player["x"] == x and player["y"] == y:
                    print("🧍", end=" ")

        # if player does not want to restart the game

        if restart == "n":
            player["hp"] = 3
            player["x"] = 5
            player["y"] = 0
            restart_game = False
            break

            # end the game loop

print("\n" * 10)
print("Thank you for playing!")
print("\n" * 5)
