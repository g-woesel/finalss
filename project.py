import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Checks if there are any winning combinations in the slot machine columns.

    Args:
        columns (list): The columns of the slot machine.
        lines (int): Number of lines bet on.
        bet (int): Bet amount on each line.
        values (dict): Symbol values.

    Returns:
        tuple: A tuple containing the total winnings and a list of winning lines.
    """
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


def get_slot_machine_spin(rows, cols, symbols):
    """
    Simulates a spin of the slot machine.

    Args:
        rows (int): Number of rows in the slot machine.
        cols (int): Number of columns in the slot machine.
        symbols (dict): Symbol count for each symbol.

    Returns:
        list: The columns of the slot machine after spinning.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Prints the slot machine columns.

    Args:
        columns (list): The columns of the slot machine.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    """
    Prompts the user to deposit money into the slot machine.

    Returns:
        int: The amount deposited.
    """
    while True:
        amount = input("How much money would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter an amount greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount


def get_number_of_lines():
    """
    Prompts the user to choose the number of lines to bet on.

    Returns:
        int: The number of lines chosen by the user.
    """
    while True:
        lines = input("How many lines would you like to bet on? (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and 3.")
        else:
            print("Please enter a valid number.")

    return lines


def get_bet():
    """
    Prompts the user to choose the bet amount per line.

    Returns:
        int: The bet amount chosen by the user.
    """
    while True:
        amount = input("How much would you like to bet per line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a bet amount between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return amount


def spin(balance):
    """
    Simulates a spin of the slot machine.

    Args:
        balance (int): The current balance in the slot machine.

    Returns:
        int: The difference between the total winnings and the total bet.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough money to bet ${total_bet}.")
        else:
            break

    print(f"Betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")
    else:
        print("You didn't win on any lines.")
    return winnings - total_bet


def main():
    """
    Main function to run the slot machine game.
    """
    print("Welcome to the Slot Machine!")
    balance = deposit()
    print(f"Your initial balance is ${balance}")
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press Enter to play or 'q' to quit: ").lower()
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You're leaving with ${balance}. Thanks for playing!")


if __name__ == "__main__":
    main()
