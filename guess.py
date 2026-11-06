import random
def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("I am thinking of a number between 1 and 100")
    while True:
        guess = input("Take a guess: ")
        attempts += 1
        try:
            guess = int(guess)
            if guess < number:
                print("Your guess is too low.")
            elif guess > number:
                print("Your guess is too high.")
            else:
                print(f"Good job! You guessed my number in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid integer.")
            again = input ("Do you want to play again? (yes/no): ")
            if again.lower() == "yes":
                play_game()
            else:
                print("Thanks for playing!")
                break
            
if __name__ == "__main__":
    play_game()            
            