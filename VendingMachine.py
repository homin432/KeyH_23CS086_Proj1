class VendingMachine:
    def __init__(self):
        self.balance = 0.0
        self.inventory = {}
        self.history = []

    def add_item(self, name, qty, price):
        self.inventory[name] = {'quantity': qty, 'price': price}

    def buy_item(self, name, dollars, quarters, dimes, nickels, pennies):
            if name in self.inventory:
                item_info = self.inventory[name]
                item_price = item_info['price']
                total_paid = dollars + (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
                if total_paid >= item_price:
                    change = total_paid - item_price
                    self.balance += item_price
                    item_info['quantity'] -= 1
                    self.history.append({'item': name, 'price': item_price})
                    self.give_change(change)
                else:
                    print("Insufficient funds.")
            else:
                print("Item not found in inventory.")
    
    #def give_change(self, change):


    

# Main program
def main():
    vending = VendingMachine()
    print("Welcome to the cool vending machine")
    command = input("Please add an Item or type \"Help\" to list all commands:").split()
    while command[0] != 'exit':
        if command[0] == 'Help':
            print("Command: balance Example: balance Description: shows the balance\n")
            print("Command: history Example: history Description: prints list of transactions\n")
            print("Command: inventory Example: inventory Description: prints available items with name and ID\n")
            print("Command: add item <str> <int> <float> Example: add item chips 2 $1.00 Description: add an item name qty price\n")
            print("Command: buy item <str> {5}<int> Example: buy item chips 1 2 2 4 3 Description: buys an item with # dollars, quarters, dimes, nickles, pennies. It also shows change given and the remaining balance with currency distribution. For change, the machine uses the largest denominator of curenncy that is available.\n")
            print("Command: exit Example: exit Description: exit the vending machine\n")
        if len(command) > 0:
            action = command[0]
            if action == 'add':
                if len(command) == 5 and command[1] == 'item':
                    name = command[2]
                    qty = int(command[3])
                    price = float(command[4][1:])  # Remove the '$' sign
                    vending.add_item(name, qty, price)
                else:
                    print("Invalid command.")

            elif action == 'buy':
                if len(command) >= 6 and command[1] == 'item':
                    name = command[2]
                    dollars = int(command[3])
                    quarters = int(command[4])
                    dimes = int(command[5])
                    nickels = int(command[6])
                    pennies = int(command[7])
                    vending.buy_item(name, dollars, quarters, dimes, nickels, pennies)
                else:
                    print("Invalid command.")
            elif action == 'exit':
                break



     
if __name__ == "__main__":
    main()