import random

choices = ["rock", "paper", "scissors"]


def get_user_choice():

    while True:

        choice = input("Choose rock, paper, or scissors: ").lower()

        if choice in choices:
            return choice

        print("Invalid choice. Try again.")


def get_computer_choice():
    return random.choice(choices)


def determine_winner(user, computer):

    if user == computer:
        return "draw"

    if (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"

    return "computer"


def play_game():

    user_score = 0
    computer_score = 0
    rounds = 5

    print("Rock Paper Scissors Game")
    print("First to win the most rounds wins!\n")

    for round_num in range(1, rounds + 1):

        print(f"Round {round_num}")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            print("You win this round!")
            user_score += 1

        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1

        else:
            print("It's a draw!")

        print(f"Score: You {user_score} - {computer_score} Computer\n")

    if user_score > computer_score:
        print("You won the game!")

    elif computer_score > user_score:
        print("Computer won the game!")

    else:
        print("The game ended in a draw.")


def main():
    play_game()


if __name__ == "__main__":
    main()
