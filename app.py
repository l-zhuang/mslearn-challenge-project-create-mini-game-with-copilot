import random

score = 0
user_input = input("Enter your choice (rock, paper, scissors): ").lower()
while user_input not in ["rock", "paper", "scissors"]:
    print("Invalid option. Please choose rock, paper, or scissors.")
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()

# Continue with the game logic here
# ...
opponent_choice = random.choice(["rock", "paper", "scissors"])
if user_input == opponent_choice:
    print("It's a tie!")
elif (user_input == "rock" and opponent_choice == "scissors") or (user_input == "scissors" and opponent_choice == "paper") or (user_input == "paper" and opponent_choice == "rock"):
    print("You won!")
    score += 1
else:
    print("You lost!")
    score -= 1
play_again = input("Do you want to play again? (yes/no): ").lower()
while play_again == "yes":
    # Restart the game
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid option. Please choose rock, paper, or scissors.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()

    # Continue with the game logic here
    # ...
    opponent_choice = random.choice(["rock", "paper", "scissors"])
    if user_input == opponent_choice:
        print("It's a tie!")
    elif (user_input == "rock" and opponent_choice == "scissors") or (user_input == "scissors" and opponent_choice == "paper") or (user_input == "paper" and opponent_choice == "rock"):
        print("You won!")
        score += 1
    else:
        print("You lost!")
        score -= 1
    play_again = input("Do you want to play again? (yes/no): ").lower()

print("Thank you for playing!")
print("Your score:", score)
