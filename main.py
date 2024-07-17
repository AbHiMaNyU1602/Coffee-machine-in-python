from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

go_on = True
while go_on:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}) ")
    if user_input == "off":
        go_on = False
    elif user_input == "report":
        coffee_maker.report()
        money.report()
    else:
        drink_chosen = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink_chosen) and money.make_payment(drink_chosen.cost):
            coffee_maker.make_coffee(drink_chosen)

