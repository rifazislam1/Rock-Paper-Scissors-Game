# Rock-Paper-Scissors-Game

# ✊ Rock Paper Scissors Game in Python

A simple command-line **Rock Paper Scissors** game built with Python. Play against the computer, test your luck, and track the scores!

This beginner-friendly project demonstrates Python functions, conditional statements, random selection, user input validation, and score tracking.

## ✨ Features

- ✊ **Rock, Paper, Scissors Gameplay** — Play against the computer.
- 🎲 **Random Computer Choice** — The computer randomly selects rock, paper, or scissors.
- 🏆 **Winner Detection** — Determines whether the player wins, the computer wins, or the game ends in a tie.
- 📊 **Score Tracking** — Tracks player and computer wins.
- ⚠️ **Input Validation** — Detects invalid choices.
- 💻 **Command-Line Interface** — Simple and easy to use.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Module:** `random`
- **Interface:** Command Line / Terminal

## 📂 Project Structure

```text
Rock-Paper-Scissors/
│
├── Rock_Paper_Scissors.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Install Python 3 on your computer.

Check whether Python is installed:

```bash
python --version
```

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/rifazislam1/Rock-Paper-Scissors.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Rock-Paper-Scissors
   ```

3. Run the game:

   ```bash
   python Rock_Paper_Scissors.py
   ```

   If necessary, use `python3` instead of `python`.

## ▶️ How to Play

1. Run the Python program.
2. Enter `rock`, `paper`, or `scissors`.
3. The computer randomly chooses its move.
4. The program displays the computer's choice.
5. The winner is announced.
6. The current score is displayed.

### Game Rules

| Player's Choice | Computer's Choice | Result |
|---|---|---|
| Rock | Scissors | Player wins |
| Paper | Rock | Player wins |
| Scissors | Paper | Player wins |
| Same choice | Same choice | Tie |
| Any losing combination | Opponent's winning choice | Computer wins |

## 💡 Example Output

```text
Enter rock, paper, or scissors: rock
Computer chose: scissors
You win!
Score -> Player: 1 | Computer: 0
```

*Note: The computer's choice and the result will vary each time you play.*

## 🧠 How It Works

- **`computer_choice()`** — Randomly selects one of the three options using Python's `random` module.
- **`determine_winner(player, computer)`** — Compares the choices and returns the result.
- **`play_game()`** — Accepts the player's input, validates it, runs the game, and displays the result.
- **`score_tracker(result)`** — Updates and displays the player and computer scores.

## 🎯 Learning Objectives

This project helps beginners learn:

- How to import and use Python modules.
- How to define and call functions.
- How to generate random choices.
- How to use `if-elif-else` statements.
- How to validate user input.
- How to use dictionaries for score tracking.
- How to organize a small Python project.

## 🔮 Future Improvements

- Add multiple rounds without restarting the program.
- Include a play-again option.
- Display the final winner after a fixed number of rounds.
- Add a graphical user interface (GUI).
- Save scores between sessions.

## 🤝 Contributing

Suggestions and contributions are welcome!

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## 📄 License

This project is open-source. You can add an [MIT License](https://opensource.org/license/mit) to allow others to reuse and modify the code under its terms.

---

**If you enjoy this project, give the repository a ⭐ on GitHub!**

*Created as a beginner-friendly Python programming project.*
