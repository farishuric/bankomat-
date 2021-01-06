
class Card():  
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


class Bankomat():
    def setcard(self, card):
        self.card = card

    def withdraw(self):
        if self.card:
            if self.card.balance > 0:
                print("Enter ammount of money you want to withdraw.")
                user_withdraw = int(input("Enter: "))
                if user_withdraw <= self.card.balance:
                    self.card.balance = self.card.balance - user_withdraw
                    print(f"You successefully withdrawed {user_withdraw}KM. Remaining funds on your account is {self.card.balance}KM")
                else:
                    print(f"You exceeded your balance. Your balance is {self.card.balance}KM.")
        else:
            print("Please try again!")

hello_message = "Welcome to ATM machine, insert card to continue."
print ("*"*len(hello_message))
print ("*", "Welcome to ATM, put in your card to continue", "*")
print ("*"*len(hello_message))

while True:
    bankomat = Bankomat()
    user_card = input("Press ENTER to put in card. ")
    pins = [1234,1411,2016]
    if user_card == "":
        user_pin = int(input("Enter your pin: "))
        if user_pin in pins:
            kartica = Card("Unicredit", 1000)
            bankomat.setcard(kartica)
            print("Acces allowed.")
            bankomat.withdraw()
            break
        else:
            print("Your pin is invalid, try again!")
            print("***Card ejected***")
            

