import random
import spin
import row
import payout

def main():
    balance = 100

    print("*************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍎 🍉🍒🍇 ")
    print("*************************")

    while balance > 0:
        print(f"Current balance: Ksh{balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()

  