import random
CHOICES = ["rock", "paper", "scissors"]
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif BEATS[player_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        elif player_choice not in CHOICES:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(CHOICES)
        print(f"Computer chose: {computer_choice}")
        result = get_winner(player_choice, computer_choice)
        print(result)
        
if __name__ == "__main__":
    play_game()            