# Slot Machine Game

This is a simple command-line-based slot machine game where players can bet on different lines and try their luck to win based on matching symbols.

---

## Features
- **Deposit Money**: Players can deposit an amount to start playing.
- **Bet on Lines**: Choose the number of lines to bet on (up to 3).
- **Place Bets**: Place a bet on each line, with a minimum and maximum limit.
- **Spin the Slot Machine**: See if you win by matching symbols across the lines.
- **Winnings Calculation**: Winnings are calculated based on the symbols matched and the bet amount.

---

## How to Play
1. **Start the game**: Run the script and deposit an amount to begin.
2. **Choose lines**: Decide how many lines (1-3) you want to bet on.
3. **Place your bet**: Enter the amount you wish to bet on each line.
4. **Spin**: The slot machine will spin and display the outcome.
5. **Check Winnings**: If you match symbols on a line, you win! Otherwise, you lose your bet.
6. **Repeat or Quit**: You can continue playing until you decide to quit or run out of balance.

---

## Game Rules
- The slot machine has 3 rows and 3 columns.
- Symbols have different values:
  - **A**: 2
  - **B**: 4
  - **C**: 6
  - **D**: 8
- The total bet is calculated as `bet amount × number of lines`.
- Winning lines are determined by matching symbols across the selected lines.
- The game continues until the player chooses to quit or runs out of balance.

---

## Setup and Running the Game

### Prerequisites
- Ensure Python is installed on your system.

### Running the Game
1. Clone or download this repository.
2. Run the script using:
   ```bash
   python main.py
   ```


## Notes
- **Minimum and Maximum Bets**: The bet amount must be between 1 and 100.
- **Balance Check**: The game checks if you have enough balance to place the bet before spinning.
- **Winning Calculation**: The winnings depend on the symbols and bet amount.

