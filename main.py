# Creating a dict for the placeholders of the game

places_dict = {"a1": " ", "a2": " ", "a3": " ",
               "b1": " ", "b2": " ", "b3": " ",
               "c1": " ", "c2": " ", "c3": " "}


#  Defining a function to draw the board every play
def draw_board():
    print('     1  2  3')
    print(f'A   {places_dict["a1"]} | {places_dict["a2"]} | {places_dict["a3"]}')
    print("   -----------")
    print(f'B   {places_dict["b1"]} | {places_dict["b2"]} | {places_dict["b3"]}')
    print("   -----------")
    print(f'C   {places_dict["c1"]} | {places_dict["c2"]} | {places_dict["c3"]}')


# Defining a function to check if any player won the game
def check_wins():
    if places_dict["a1"] == "X" and places_dict["a1"] == places_dict["a2"] == places_dict["a3"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["a1"] == "O" and places_dict["a1"] == places_dict["a2"] == places_dict["a3"]:
        print("Player 2 Wins!")
        return False
    elif places_dict["a1"] == "X" and places_dict["a1"] == places_dict["b1"] == places_dict["c1"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["a1"] == "O" and places_dict["a1"] == places_dict["b1"] == places_dict["c1"]:
        print("Player 2 Wins!")
        return False
    elif places_dict["a1"] == "X" and places_dict["a1"] == places_dict["b2"] == places_dict["c3"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["a1"] == "O" and places_dict["a1"] == places_dict["b2"] == places_dict["c3"]:
        print("Player 2 Wins!")
        return False
    elif places_dict["a2"] == "X" and places_dict["a2"] == places_dict["b2"] == places_dict["c2"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["a2"] == "O" and places_dict["a2"] == places_dict["b2"] == places_dict["c2"]:
        print("Player 2 Wins!")
        return False
    elif places_dict["a3"] == "X" and places_dict["a3"] == places_dict["b2"] == places_dict["c1"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["a3"] == "O" and places_dict["a3"] == places_dict["b2"] == places_dict["c1"]:
        print("Player 2 Wins!")
        return False
    elif places_dict["a3"] == "X" and places_dict["a3"] == places_dict["b3"] == places_dict["c3"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["a3"] == "O" and places_dict["a3"] == places_dict["b3"] == places_dict["c3"]:
        print("Player 2 Wins!")
        return False
    elif places_dict["b1"] == "X" and places_dict["b1"] == places_dict["b2"] == places_dict["b3"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["b1"] == "O" and places_dict["b1"] == places_dict["b2"] == places_dict["b3"]:
        print("Player 2 Wins!")
        return False
    elif places_dict["c1"] == "X" and places_dict["c1"] == places_dict["c2"] == places_dict["c3"]:
        print("Player 1 Wins!")
        return False
    elif places_dict["c1"] == "O" and places_dict["c1"] == places_dict["c2"] == places_dict["c3"]:
        print("Player 2 Wins!")
        return False
    else:
        return True


# Print the welcome message
print("Welcome to tic tac toe: Player 1 will play with 'X', Player 2 will play with 'O'.\n")

# Defining a variable to stop the game when somebody exits or wins
game_on = True

# Initiating a while loop to play the game
while game_on:

    # Draw the board in the loop
    draw_board()
    p1_valid = False
    p2_valid = False

    # Initiating another while loop to check if the choice is valid
    while not p1_valid:
        p1_choice = input("What place do you want to go Player 1? / Write 'Exit' to quit the game.\n").lower()
        # Check if p1 choose to exit game
        if p1_choice == "exit":
            game_on = False
            break

        # Change the placeholder to p1_choice and validate the alternative
        elif p1_choice in places_dict and places_dict[p1_choice] == " ":
            places_dict[p1_choice] = "X"
            p1_valid = True

        else:
            print("Invalid choice Player 1, please choose again.")

    # Check if player 1 have won the game and exit in this case
    game_on = check_wins()
    if not game_on:
        draw_board()
        break

    draw_board()

    # Another while loop to check if player 2 input is valid
    while not p2_valid:
        p2_choice = input("What place do you want to go Player 2? / Write 'Exit' to quit the game.\n").lower()
        if p2_choice == "exit":
            game_on = False
            break

        # Change the placeholder to p2_choice
        elif p2_choice in places_dict and places_dict[p2_choice] == " ":
            places_dict[p2_choice] = "O"
            p2_valid = True

        else:
            print("Invalid Choice, Player 2, please choose again.")

    # Check if player 2 have won the game and ending the game in case it has happened
    game_on = check_wins()
    if not game_on:
        draw_board()
        break
