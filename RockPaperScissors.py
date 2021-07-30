import random




# Get the user's move choice
userSelection = input("Select your move:\n"
                      + "1: Rock\n"
                        "2: Paper\n"
                        "3: Scissors\n")


# Create the list of moves for computer to use
possibleMoves = ["rock", "paper", "scissors"]

# Generating random input for the computer for the game
computerMove = random.choice(possibleMoves)

# Choice comparison
# If they pick the same thing
if userSelection.lower() == computerMove.lower():
    print("The user picked: " + userSelection + "\n"
          + "The computer picked " + computerMove)
    print("Tie! Play again!")

# If user picks rock and they pick scissors
elif userSelection.lower() == "rock":
    print("The user picked: " + userSelection + "\n"
          + "The computer picked " + computerMove)
    if computerMove.lower == "Scissors":
        print("You win!")
    elif computerMove.lower() == "paper":
        print("You lose!")

# if user picks paper and they pick scissors
elif userSelection.lower() == "paper":
    print("The user picked: " + userSelection + "\n"
          + "The computer picked " + computerMove)
    if computerMove.lower == "rock":
        print("You win!")
    elif computerMove.lower() == "scissors":
        print("You lose!")

# if user picks scissors and they pick paper
elif userSelection.lower() == "scissors":
    print("The user picked: " + userSelection + "\n"
          + "The computer picked " + computerMove)
    if computerMove.lower == "paper":
        print("You win!")
    elif computerMove.lower() == "Rock":
        print("You lose!")
else:
    print("Invalid")
