import random

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif ((player == 'rock' and computer == 'scissors') or
          (player == 'paper' and computer == 'rock') or
          (player == 'scissors' and computer == 'paper')):
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    player = input("Enter rock, paper, or scissors: ").lower()
    if player not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        return None
    
    computer = computer_choice()
    print(f"Computer chose: {computer}")
    
    result = determine_winner(player, computer)
    print(result)
    return result

score = {"player": 0, "computer": 0}

def score_tracker(result):
    global score

    if result == "You win!":
        score["player"] += 1
    elif result == "Computer wins!":
        score["computer"] += 1

    print(f"Score -> Player: {score['player']} | Computer: {score['computer']}")
    
    
result = play_game()
if result is not None:
    score_tracker(result)
    