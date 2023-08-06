import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(total_rounds):
    print("Let's play Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    for round in range(1, total_rounds + 1):
        print(f"\nRound {round}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result.lower():
            if "you" in result.lower():
                user_score += 1
            else:
                computer_score += 1

    print("\nGame Over!")
    print(f"Your final score: {user_score}")
    print(f"Computer's final score: {computer_score}")
    if user_score == computer_score:
        print("It's a tie!")
    elif user_score > computer_score:
        print("Congratulations, you win!")
    else:
        print("Sorry, computer wins!")

if __name__ == "__main__":
    total_rounds = int(input("Enter the number of rounds you want to play: "))
    play_game(total_rounds)
