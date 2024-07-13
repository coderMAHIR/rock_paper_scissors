import random
def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    if user_choice.lower() in ["rock", "paper", "scissors"]:
        return user_choice.lower()
    else:
        print("Invalid choice. Please try again.")
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer Wins!"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer Chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Please enter yes or no: ").lower()
            if play_again == "yes":
                print("Let's play again!")
                continue  # Go back to the start of the loop and play again
            else:
                print("Thanks for playing!")
            break  # Exit the loop and end the game
if __name__ == "__main__":
    play_game()
