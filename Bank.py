import random
class Bank:
    def __init__(self) -> None:
        self.admins = []
        self.users = []
        self.is_loan_able = True
        self.total_loan = 0
        self.bank_blance = 0

    def create_user(self, name, email, address, account_type):
        account_number = 'BANK_A_' + str(random.randint(500, 1000))
        user = User(name, email, address, account_number, account_type)
        self.users.append(user)
        return user

    def add_admin(self, name, email, address):
        admin_id = 'BANK_A_' + str(random.randint(200, 300))
        admin = Admin(name, email, address, admin_id)
        self.admins.append(admin)
        return admin
    
    def total_bank_balance(self):
        return self.bank_blance

    def total_loan_amount(self):
        return self.total_loan

    def delete_account(self, account_number):
        user = self.find_user(account_number)
        if user:
            self.users.remove(user)
            return f'Removed user account number : {account_number}'
        return f'{account_number} user not found'

    def users_list(self):
        return self.users


    def off_loan_feature(self):
        self.is_loan_able = not self.is_loan_able
        if self.is_loan_able:
            return f'Loan is enabled'
        else:
            return f'Loan is not enabled'

    def find_user(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                return user
        return None

    def find_admin(self, admin_id):
        for admin in self.admins:
            if admin.admin_id == admin_id:
                return admin
        return None

class Person:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address

class User(Person):
    def __init__(self, name, email, address, account_number, account_type) -> None:
        super().__init__(name, email, address)
        self.account_number = account_number
        self.account_type = account_type
        self.transition_depostit = 0
        self.transition_withdraw = 0
        self.transition_transfer = 0
        self.loan = 0
        self.balance = 0

    def deposit(self, amount, bank):
        if amount > 0:
            self.balance += amount
            self.transition_depostit += amount
            bank.bank_blance += amount
            return f'You have deposited : {amount} \n Current balance : {self.balance}'
        else:
            return "Enter a valid amount"

    def withdraw(self, amount, bank):
        if amount <= self.balance:
            self.balance -= amount
            self.transition_withdraw += amount
            bank.bank_blance -= amount
            return f'Your withdrawal : {amount} \n Current Balance:{self.balance}'
        else:
            return 'Withdrawal amount exceeded'

    def check_balance(self):
        return self.balance

    def transfer_money(self, receiver_acc_no, amount, bank):
        receiver = bank.find_user(receiver_acc_no)
        if receiver:
            if self.balance > amount:
                self.balance -= amount
                self.transition_transfer += amount
                receiver.balance += amount
                return f'{amount} Money transfered to {receiver_acc_no} \n current balance : {self.balance}'
            return f'Not enough money to transfer'
        return f'Receiver not found'

    def transition(self):
        return f'Total deposit : +{self.transition_depostit}\n Total withdraw : -{self.transition_withdraw}\n Total transfer : -{self.transition_transfer}'

    def take_loan(self, amount, bank):
        if bank.is_loan_able and self.loan <= 2:
            if bank.bank_blance > amount:
                self.balance += amount
                self.loan += 1
                bank.total_loan += amount
                return f'Your loan if given amount : {amount} \n Current balance: {self.balance}'
            return f'Sorry, not enough money.'
        else:
            return f'Loan not abailable.'
        
class Admin(Person):
    def __init__(self, name, email, address, admin_id) -> None:
        self.admin_id = admin_id
        super().__init__(name, email, address)