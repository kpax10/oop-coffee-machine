from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

coffee = True

while coffee:
    order = input("What do you want to order? latte/espresso/cappuccino ").lower()
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        coffee = False
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
