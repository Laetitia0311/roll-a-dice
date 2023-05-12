import random

response = input ("Do you want to roll a dice (y/n)?")

while response == "y":
    # Roll the dice
    dice_value = random.randint(1, 6)
    # Print the output
    print("+-------+")
    if dice_value == 1:
        print("|       |")
        print("|   *   |")
        print("|       |")
    elif dice_value == 2:
        print("| *     |")
        print("|       |")
        print("|     * |")
    elif dice_value == 3:
        print("| *     |")
        print("|   *   |")
        print("|     * |")
    elif dice_value == 4:
        print("| *   * |")
        print("|       |")
        print("| *   * |")
    elif dice_value == 5:
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
    elif dice_value == 6:
        print("| * * * |")
        print("|       |")
        print("| * * * |")
    print("+-------+")

    # Ask the user to continue or exit
    response = input("Do you want to roll the dice again? (y/n) ").lower()

print("Thank you for playing!")