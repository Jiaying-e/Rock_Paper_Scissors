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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_source(order_ingredients):
    """Return true when order can be made and return false when resource is insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def total_price():
    """Return the calculated coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.10
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total


def check_transaction(received, cost):
    """Return true when the payment is successful"""
    if received >= cost:
        change = round(received-cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money returned")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your{drink_name}")


is_continue = True
while is_continue:
    choice = input("What would you like?(espresso/latte/cappuccino):")
    if choice == "off":
        is_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${profit}")
    else:
        drink = MENU[choice]
        if check_source(drink['ingredients']):
            payment = total_price()
            if check_transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])





