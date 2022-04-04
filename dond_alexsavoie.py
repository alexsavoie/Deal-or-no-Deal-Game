import time
import random
import sys

# Instruction to end game and stop the program


def end_game():
    sys.exit()


# The amount won by the player, initialize to 0
prize = 0

# Will be used to display remaining cash in cases
default_money_cases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
                       10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]


# Randomizing money cases and assigning them to a unique case number from 1 to 26 (0 to 25, really)
money_cases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
               10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
random.shuffle(money_cases)

available_cases = {}
for i in range(26):
    available_cases[i] = money_cases[i]


# The case the player will choose to keep for the game
player_case = {}

# Player chosen case get stored in player_case {case_number : $}


def own_case_selection():
    case_number = 0
    while (case_number > 26 or case_number < 1):
        case_number = input("Choose your case number : ")
        case_number = int(case_number)
        if (case_number > 26 or case_number < 1):
            print("Wrong input! Please input a number between 1 and 26")
    player_case[case_number-1] = available_cases[case_number-1]
    available_cases.pop(case_number-1)
    print("You chose case number ", case_number,
          ", let's put this case on the side for now.")

# Selecting a case and removing it from the available_cases


def case_selection(cases, display_cases):
    case_number = 0
    case_number = input("Choose a case number : ")
    case_number = int(case_number) - 1
    if case_number in cases:
        print("\nThe case number", case_number+1,
              "had", cases[case_number], "$ inside.")
        X = display_cases.index(cases[case_number])
        display_cases[X] = 0
        cases.pop(case_number)
    elif (case_number+1 > 26 or case_number+1 < 1):
        print("\nInvalid input, please choose a case between 1 and 26")
        case_selection(cases, display_cases)
    else:
        print("\nCase already selected, please choose another one")
        case_selection(cases, display_cases)

# Dealer makes an offer to the player (90% of the average of the remaining cases)


def dealer_deal():
    time.sleep(2)
    print("\nThe banker is calling ...\n")
    time.sleep(1)
    offer = (sum(available_cases.values())/len(available_cases))*0.9
    print("He offers you a sum of", round(offer, 2), "$")

    while True:
        query = input(
            '"Do you accept the offer?\nPress Yes to accept the offer or No to continue playing : ')
        Fl = query[0].lower()
        if query == '' or not Fl in ['y', 'n']:
            print('Please answer with yes or no!')
        else:
            break
    if Fl == 'y':
        print("\nGame over! You won ", round(offer, 2),
              "$!\nThank you for playing Deal or No Deal.")
        time.sleep(5)
        end_game()
    if Fl == 'n':
        print("\nLet's continue!\n")


# Displays a board with the remaing sum of cash
def print_cash_remaining():
    print("\n\tMONEY BOARD\n")
    for a in range(26):
        if default_money_cases[a] == 0:
            default_money_cases[a] = "-----"
    for i in range(13):
        print(default_money_cases[i], "\t\t", default_money_cases[i+13], "\n")


# Display the remaning cases
def print_cases_number(list):
    print("\nHere are the remaining cases: ")
    list_of_cases = list.keys()
    adjusted = [x + 1 for x in list_of_cases]
    values = [str(item) for item in adjusted]
    print(', '.join(values), "\n")

# Opening cases x times


def open_case_round(case_to_open, display_cases):
    for i in range(case_to_open):
        print_cases_number(available_cases)
        case_selection(available_cases, display_cases)


# Start of the game
print("WELCOME TO DEAL OR NO DEAL!")

time.sleep(1)

print("Let's begin by selecting the case you wish to keep.")
own_case_selection()


open_case_round(6, default_money_cases)

print_cash_remaining()

time.sleep(1)

dealer_deal()
