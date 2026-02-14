MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

penny = 0.01
dime = 0.1
nickel = 0.05
quarter = 0.25

profit = 0


def start():
    valid_options = {"espresso", "latte", "cappuccino", "report", "off"}
    while True:
        choice = input("What would you like? ").lower()
        if choice in valid_options:
            return choice
        print("Invalid option, please try again.")


def check_resources(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    p = int(input("How many pennies? ")) * penny
    q = int(input("How many quarters? ")) * quarter
    d = int(input("How many dimes? ")) * dime
    n = int(input("How many nickels? ")) * nickel
    return p + q + d + n


def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")


machine_on = True

while machine_on:
    choice = start()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")

    else:
        if check_resources(choice):
            money = process_coins()
            price = MENU[choice]["cost"]

            if money < price:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(money - price, 2)
                profit += price
                print(f"Here is ${change} in change.")
                make_coffee(choice)
