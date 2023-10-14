from Bank import Bank
def main():
    bank = Bank()
    
    admin = bank.add_admin('Bilkis', 'bilki@gmail.com', 'Chittagong')
    print(f"Admin: {admin.name} and admin id: {admin.admin_id}")
    user_1 = bank.create_user('Akter', 'akter@gmail.com', 'Dijanpur', "Saving")
    print(f"User id {user_1.name}: {user_1.account_number}")
    user_2 = bank.create_user('Dalia', 'dalia@gmail.com', 'Vasancor', "Current")
    print(f"User id {user_2.name}: {user_2.account_number}")

    while True:
        print('\nWelcome to bank')
        print('\n1.User login')
        print('2.Admin login')
        print('3.Exit')
        choice = int(input('\nEnter the option : '))
        if choice == 1:
            account_number = input('please, enter account Number: ')
            user = bank.find_user(account_number)
            if user:
                print(f'\nWelcome user: {user.name} Account Number: {user.account_number}\n')
                while True:
                    print('1.Deposit')
                    print('2.Withdraw')
                    print('3.Check balance')
                    print('4.Take loan')
                    print('5.Transfer funds')
                    print('6.Transition history')
                    print('7.Logout')
                    ch = int(input('Enter your choice : '))
                    if ch == 1:
                        amount = float(input('Enter amount : '))
                        print(user.deposit(amount, bank))
                    elif ch == 2:
                        amount = float(input('Enter amount : '))
                        print(user.withdraw(amount, bank))
                    elif ch == 3:
                        print(user.check_balance())
                    elif ch == 4:
                        amount = float(input('Enter amount : '))
                        print(user.take_loan(amount, bank))
                    elif ch == 5:
                        amount = float(input('Enter amount : '))
                        receiver_account_number = input("Enter the recipient's account number: ")
                        print(user.transfer_money(receiver_account_number, amount, bank))
                    elif ch == 6:
                        print(user.transition())
                    elif ch == 7:
                        break
                    else:
                        print('Enter a valid choice')
            else:
                print('User not found')
        elif choice == 2:
            admin_id = input('Enter your admin Id : ')
            admin = bank.find_admin(admin_id)
            if admin:
                print(f'\nWelcome Admin : {admin.name} ID: {admin.admin_id}\n')
                while True:
                    print('1.Delete account')
                    print('2.User account List')
                    print('3.Check your total bank balance')
                    print('4.Check The Total Loan Amount')
                    print('5.Update loan feature')
                    print('6.Logout')
                    ch = int(input('Enter your option : '))
                    if ch == 1:
                        user_account_number = input('User account number : ')
                        print(bank.delete_account(user_account_number))
                    elif ch == 2:
                        users = bank.users_list()
                        for user in users:
                            print(f'Username: {user.name} account_no: {user.account_number} and balance: {user.balance}')
                    elif ch == 3:
                        print(bank.total_bank_balance())
                    elif ch == 4:
                        print(bank.total_loan_amount())
                    elif ch == 5:
                        print(bank.off_loan_feature())
                    elif ch == 6:
                        break
                    else:
                        print('Enter a valid option')
            else:
                print('There is no admin found')
        elif choice == 3:
            break
        else:
            print('Enter a valid Option')

if __name__ == "__main__":
    main()