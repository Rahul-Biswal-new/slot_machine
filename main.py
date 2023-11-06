MAX_LINES = 3


def deposite():
    while True:
        amount = input("what would you like to deposite?")
        if (amount.isdigit()):
            amount= int(amount)
            if(amount>0):
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("PLEASE ENTER A NUMBER")
    return amount


def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on (1-" + str(MAX_LINES)+ ")? ")
        if (lines.isdigit()):
            lines= int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("ENTER VALID NUMBERE OF LINES")
        else:
            print("PLEASE ENTER A NUMBER")
    return lines


def main():
    balance = deposite()
    lines = get_number_of_lines()


main()