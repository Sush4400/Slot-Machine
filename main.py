import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3


symbol_value = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbol):
    all_symbols = []
    for symbol, symbol_count in symbol.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



def deposit():
    while True:
        try:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 0:
                return amount
            print('Amount must be greater than 0')
        except:
            print("Please enter a number")


def get_number_of_lines():
    while True:
        try:
            lines = int(input(f"Enter the number of lines to bet on (1-{MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            print('Enter valid number of lines')
        except:
            print("Please enter a number")
        

def get_bet():
    while True:
        try:
            amount = int(input(f"How much you want to bet on each line ({MIN_BET}-{MAX_BET}): "))
            if MIN_BET <= amount <= MAX_BET:
                return amount
            print(f'Enter bet amount between {MIN_BET} to {MAX_BET}')
        except:
            print("Please enter a number")


def spin(balance):
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"You don't have enough balance to bet. \nYour balance: ₹{balance} \nBetting balance: ₹{total_bet}")
        else:
            break
        

    print(f"You are betting ₹{bet} on {lines} lines. Total bet is equal to ₹{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_value)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings:
        print(f"You won ₹{winnings}.")
        print(f"You won on lines:", *winning_lines)
    else:
        print("You lose...")
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ₹{balance}")


    # print(balance, lines, bet)


if __name__ == '__main__':
    main()