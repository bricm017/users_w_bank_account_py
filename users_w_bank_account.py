class BankAccount:
    bank_name = "Isla Nublar Credit Union"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self 
    def display_account_info(self):
        print("Balance: " , self.balance)
    def yield_interest(self):
        self.balance += (self.balance * int_rate)

class User:
    def __init__(self, name, email_address, account_name):
        self.name = name
        self.email = email_address
        self.account_name = account_name
        self.account = BankAccount(int_rate=0.02, balance=0)
    def display_account_info(self):
        print("User: " , self.name, " Email: " , self.email, " Account: " , self.account_name)
    def display_user_balance(self):
        print("User: " , self.name, self.account.balance)
        return self
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    def withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    def yield_interest(self):
        self.account.yield_interest()

Sarah = User("Sarah","sarahnmaze@gmail.com", "Sarah!86")
Andy = User("Andy","andystoyz@gmail.com", "Gotafriend95")
#User 1: make 3 deposits and 1 withdrawal, then yield interest and display the account's info
Sarah.deposit(200).deposit(2660).deposit(500).withdraw(300).display_account_info()
Sarah.display_user_balance()
#User 2: make 2 deposits and 4 withdrawals, then yield interest and display the account's info
Andy.deposit(1000).deposit(50660).withdraw(2000).withdraw(500).withdraw(1000).withdraw(300).display_account_info()
Andy.display_user_balance()