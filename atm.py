class Atm(object):
    def __init__(self,pin,cardnumber,balance):
        self.PIN=pin
        self.cardnum=cardnumber
        self.bankBalance=balance
     
    def balance(self):
        print("your bank balance =>",self.bankBalance)
    def withdraw(self,amount):
        print("withdrawen =>",amount,"remaining balance=>",self.bankBalance-amount)
    
person1=Atm(712368176,123456,100000)

person1.balance()
person1.withdraw(1000)