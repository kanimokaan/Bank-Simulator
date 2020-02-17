# importing time library for time.sleep code below

import time


# dictionary has username(s) and password(s)

users = {'manager': 'manager123', 'ahmet': 'ahmet123', 'a': 'a'}  # ad, sifre

# dictionary has username(s) and balance(s)

account_holders = {'manager': 100, 'ahmet': 50, 'a': 0}  # ad, para

# dictionary had admin username(s) and password(s)

admins = {'admin': 'abc123', 'a': 'a'}

#
# dictionaries to use in different menu functions

main_menu = {1: 'Check Balance', 2: 'Transfer Money', 3: 'Deposit', 4: 'Withdraw', 5: 'Close Account',
             6: 'Update Password', 7: 'See the Latest Transactions', 8: 'Admin Menu', 9: 'Quit'}
menu1 = {1: 'Go to the main menu', 2: 'Quit'}
menu2 = {1: 'Load Customer Account From Data', 2: 'Create Account', 3: 'Close Account', 4: 'Search for an Account',
         5: 'See The Stats', 6: 'Go to the Main Menu'}
menu3 = {1: 'Go to the admin menu', 2: 'Quit'}


#
# function to use after user transactions

def menu1_f():
    print 'What do you want to do next?'

    # prints the keys and values of menu1 dictionary to show menu
    for i in menu1:
        print str(i) + '. ' + menu1[i]

    islem1 = raw_input("Your choice: ")  # asking to enter a number of any option from menu

    if islem1 == '*':  # checking if the secret code entered
        menu()

    elif int(islem1) == 1:  # checking if the 1st option of menu choosen
        menu()

    elif int(islem1) == 2:  # checking if the 1st option of menu choosen. if it is, terminates the program
        print 'Program Terminated !'

    else:    # checking if entered value is valid. if it is not, restarts the function
        print 'Please try again!'
        menu1_f()


#
# function to use after admin transactions

def menu1_f_a():
    print 'What do you want to do next?'

    # prints the keys and values of menu1 dictionary to show menu
    for i in menu3:
        print str(i) + '. ' + menu3[i]

    islem1 = raw_input("Your choice: ")    # asking to enter a number of any option from menu

    if islem1 == '*':    # checking if the secret code entered
        menu()

    elif int(islem1) == 1:  # checking if the 1st option of menu choosen
        a_menu()

    elif int(islem1) == 2:  # checking if the 1st option of menu choosen. if it is, terminates the program
        print 'Program Terminated !'

    else:    # checking if entered value is valid. if it is not, restarts the function
        print 'Please try again!'
        menu1_f_a()


#
# Openning sentence

print 'Welcome to Banking Account Management Tool (v. 1.0)\nPlease log in by providing your user credentials:'


#
def login():  # function to be used in log in action

    # making the codes which are going to use later in other functions 'global'

    global username
    global transactions
    global transactions_list

    # asking user to enter username and password

    username = raw_input("Username: ")
    password = raw_input("Password: ")

    if username in users and password == users[username]:  # checking if entered username is exist 'and' entered password matches with the right one

        print 'Welcome, ' + username + '! Please choose one of the following options by\nentering the corresponding menu number.'  # greeting

        #creating a list to append transactions tuples
        transactions_list = []

        #creating a dictionary to match transaction list with username. this is for making easier to read and write codes about transactions
        transactions = {username: transactions_list}



        menu()    #running menu function

    else:    #when username and/or password is not correct, runs login function again
        print 'Your user name and/or password is not correct. Please try again!'
        login()


################


def menu():
    # prints the keys and values of main_menu dictionary to show menu
    for i in main_menu:
        print str(i) + '. ' + main_menu[i]

    islem0 = raw_input("Please make your selection: ")    #asking for what user want in menu

    if int(islem0) > len(main_menu):    #if the given number greater than our last number show error
        print str(islem0) + ' is not a valid entry. Please choose from the above menu.'  #what user see when he/she write invalid number
        menu()#running the menu function
    # 1
    elif int(islem0) == 1:  #if the given number is 1, then it's works
        print '===== Check Balance =====\nYou have ' + str(account_holders[username]) + ' TL in your account.'#show the balance of user
        menu1_f()#running the menu1_f function
    # 2
    elif int(islem0) == 2:#if the given number is 2, then it work
        def transfer():#define the transfer function
            alici1 = raw_input("Please enter recipient: ")#asking who you want to send money to
            if alici1 not in account_holders and alici1 != '*':#if the entered not in account list and not a *, then show error
                print alici1 + ' is not a valid recipient. Please try again.'#what user see when he/she write invalid enter
                transfer()#running the transfer function
            elif alici1 in account_holders:#if the entered in the account list then, it's works
                transfer_amount = raw_input("Please enter the amount: ")#ask for how much user want to send
                if transfer_amount == '*':#if entered equel a * then,
                    menu()#running the menu function
                else:#if user entered number
                    print transfer_amount + ' TL will be transferred to ' + alici1 + ' today.'#show entered money is being sent to recipient
                    transfer_onay = raw_input("Do you approve (yes/no?): ")#ask if user approve
                    if transfer_onay == 'yes':#if user enter yes, then it's work
                        account_holders[username] = account_holders[username] - int(transfer_amount)#withdraw the entered amount money from user
                        account_holders[alici1] = account_holders[alici1] + int(transfer_amount)#deposit the entered money to recipient
                        print transfer_amount + ' TL has been transferred to ' + alici1 + '. Your current balance is ' + str(
                            account_holders[username]) + ' TL.'#show enetered money is transferred to recipient

                        transfer_transaction = ("Transfer", transfer_amount, alici1, account_holders[username])#creatig a tupple to append transaction history
                        transactions_list.append(transfer_transaction)#appendeing transaction tupple to transaction history list
                        menu1_f()#running the menu1_f function

                    elif transfer_onay == 'no':#if user enter no, then it's work
                        print 'Your transfer request has canceled.'#show this line after enter the no
                        menu1_f()#running the menu1_f function
                    elif transfer_onay == '*':#if user enter *, not a yes/no then its work
                        menu()#running the menu function
            elif alici1 == '*':#if user enter *, not a yes/no then its work
                menu()#running the menu function

        transfer()#running the transfer function
    # 3
    elif int(islem0) == 3:#if the given number is 3, then it's work
        print '===== Deposit Money ====='#greetings
        deposit_amount = raw_input("Please enter the amount")#asking for the how much user deposit the money
        if deposit_amount == '*':#if entered =* then it's work
            menu()#running the menu function
        else:#if entered is number then it's work
            account_holders[username] = account_holders[username] + int(deposit_amount)#deposit to entered money to user
            print deposit_amount + ' TL has been deposited to your account. Your current balance is ' + str(
                account_holders[username]) + ' TL.'#show entered money deposited the user

            deposit_transaction = ("Deposit", deposit_amount, account_holders[username])#creatig a tupple to append transaction history
            transactions_list.append(deposit_transaction)#appendeing transaction tupple to transaction history list

            menu1_f()#running the menu1_f function
        # 4
    elif int(islem0) == 4:#if the given number is 4, then it's work
        print '===== Withdraw Money ====='#greetings
        withdraw_amount = raw_input("Please enter the amount")#asking for the how much user withdraw the money
        if withdraw_amount == '*':#if entered =* then it's work
            menu()#running the menu function
        else:#if entered is number then it's work
            account_holders[username] = account_holders[username] - int(withdraw_amount)#withdraw to entered money to user
            print withdraw_amount + ' TL has been withdrawn from your account. Your current balance is ' + str(
                account_holders[username]) + ' TL.'#show entered money withdrawn the user

            withdraw_transaction = ("Withdrawal", withdraw_amount, account_holders[username])#creatig a tupple to append transaction history
            transactions_list.append(withdraw_transaction)#appendeing transaction tupple to transaction history list

            menu1_f()#running the menu1_f function
        # 5
    elif int(islem0) == 5:#if the given number is 5, then it's work
        def close_account0():
            if account_holders[username] != 0:#check the money in account then if its not a 0,show error
                print '===== Close Your Account =====\nSorry, we cannot close your account at this point, as you\n' \
                      'still have some balance in your account. You should\nwithdraw this balance before closing your account.'#error message
            elif account_holders[username] == 0:#check the money in account then if its 0,then its work
                print '===== Close Your Account ====='#greetings
                closing_onay = raw_input("Do you approve (yes/no?)")#ask if user approve
                if closing_onay == 'yes':#if entered is yes then its work
                    account_holders.pop(username)#removing the account from account holders
                    print 'Your account has been closed now, and your session has ended.\nThanks for being our customer.'#show the user's account closed

                elif closing_onay == 'no':#if entered is no then its work
                    print 'Your account closing request has been canceled.'#show the your request canceled
                    menu()
                elif closing_onay == '*':#if entered is *
                    menu()#running the menu function
                else:
                    print 'Please try again!'
                    close_account0  ()
        close_account0()


    # 6
    elif int(islem0) == 6:#if the given number is 6, then it's work
        def update_pw():#define the update_pw function
            current_password = raw_input("Please enter your current password: ")#asking for the current password
            if current_password == users[username]:#if entered equels to current password
                new_password = raw_input("Please enter your new password: ") #asking for enter the new password
                if new_password == '*':#if entered=* then its work
                    menu()#running the menu function
                else:
                    new_password_p = raw_input("Please re-enter your new password: ")#asking for re-enter the new password
                    if new_password_p == '*':#if entered=* then its work
                        menu()#running the menu function
                    else:
                        if new_password == new_password_p:#if two entered equels with each other
                            users[username] = new_password#changed the user's password
                            print 'Your password has been successfully updated.'#show the password is changed
                            menu1_f()  # running the menu1_f function
                        else:#if two entered not equels with each other
                            print "Sorry, your new password entries do not match!\nPlease try again!"#show the error
                            update_pw()#runnning the update_pw function
            elif current_password != users[username] and current_password != '*':#check, dont match the password
                print 'Sorry, your password is wrong!\nPlease try again!'#show the password dont match
                update_pw()#runnning the update_pw function
            elif current_password == '*':#if entered=* then its work
                menu()#running the menu function

        update_pw()#running the update_pw function

    # 7
    elif int(islem0) == 7:#if the given number is 7, then it's work
        print '===== See the Latest Transactions =====\nHere, you may view your latest transactions starting from the most recent one.'#greetings

        N = raw_input("Please enter how many transactions you want to see:")#choose how many trancsactions do you want to see

        transactions_list_1 = []#creating free transaction list to read reverse mood

        if N == '*':#if entered=* then its work
            menu()#running the menu function
        else:
            N = int(N)#transfer to N to integer form
            if N > len(transactions_list):#check N is greater then transaction numbers, if it is then work
                print 'You have only "' + str(len(transactions_list)) + '" transactions.'#show the how many transaction you had
                N = len(transactions_list)#N is become your total number trancision

            for i in range(N): #read transactions list as much as we want

                if transactions[username][len(transactions_list) - i - 1][0] == "Transfer":#check transaction's type is transfer
                    #shaping the transaction in sentence
                    hist = transactions[username][len(transactions_list) - i - 1][0] + ': ' + str(
                        transactions[username][len(transactions_list) - i - 1][1]) + ' TL, Recipient: ' + \
                           transactions[username][len(transactions_list) - i - 1][2] + ', Balance: ' + str(
                        transactions[username][len(transactions_list) - i - 1][3]) + ' TL'
                    transactions_list_1.append(hist)#append the sentence above to transactions_list_1

                elif transactions[username][len(transactions_list) - i - 1][0] == "Deposit":#check transaction's type is deposit
                    # shaping the transaction in sentence
                    hist = transactions[username][len(transactions_list) - i - 1][0] + ': ' + str(
                        transactions[username][len(transactions_list) - i - 1][1]) + ' TL, Balance: ' + str(
                        transactions[username][len(transactions_list) - i - 1][2]) + ' TL'
                    transactions_list_1.append(hist)#append the sentence above to transactions_list_1

                elif transactions[username][len(transactions_list) - i - 1][0] == "Withdrawal":#check transaction's type is withdrawn
                    # shaping the transaction in sentence
                    hist = transactions[username][len(transactions_list) - i - 1][0] + ': ' + str(
                        transactions[username][len(transactions_list) - i - 1][1]) + ' TL, Balance: ' + str(
                        transactions[username][len(transactions_list) - i - 1][2]) + ' TL'
                    transactions_list_1.append(hist)#append the sentence above to transactions_list_1

            for q in range(len(transactions_list_1)):#prints transaction
                print transactions_list_1[q]

            menu1_f()


        # 8
    elif int(islem0) == 8:#if the given number is 8, then it's work
        print '===== Admin Operations ====='#greetings

        def admin_login():#define the admin_login function
            global a_username#make the a_username valid for this function
            a_username = raw_input("User Name: ")#asking for a username
            if a_username == '*':#if entered=*
                menu()#running the menu function
            else:
                a_password = raw_input("Password: ")#asking for a password
                if a_password == '*':#if entered=*
                    menu()#running the menu function
                else:
                    if a_username in admins and a_password == admins[a_username]:#check the entered username and entered password equels to admin's one

                        print 'Welcome!',#greetings
                        a_menu()#running the a_menu function
                    else:
                        print 'Your user name and/or password is not correct. Please try again!'#show the error
                        admin_login()#running the admin_login function

        global a_menu#make the a_menu a valid for this function

        def a_menu():#start the a_menu funciton

            print 'Please choose one of the following options by\nentering the corresponding menu number.'#show the asking for selection in menu
            for a in menu2:
                print str(a) + '. ' + menu2[a]

            islem2 = raw_input("Please make your selection: ")

            if islem2 == '*':
                menu()
            elif int(islem2) > len(menu2):
                print islem2 + ' is not a valid entry. Please choose from the above menu.'
                a_menu()
            ##1
            elif int(islem2) == 1:
                print '===== Admin: Load Customer Account Data ====='
                print 'Loading...\n'
                time.sleep(1)

                customer_accounts = open("customer_accounts.txt", "w")
                for i in account_holders:
                    customer_accounts.write(i + '***' + users[i] + '***' + str(account_holders[i]) + "\n")
                customer_accounts.close()
                customer_accounts = open("customer_accounts.txt", "r")

                print 'The account data for ' + str(len(account_holders)) + ' customers have been loaded.'

                print customer_accounts.read()
                customer_accounts.close()
                menu1_f_a()
            ##2
            elif int(islem2) == 2:
                print '===== Admin: Create Account ====='

                def create_account():
                    new_account_username = raw_input('Please enter account holder name: ')
                    if new_account_username in account_holders:#check if account exist
                        print 'This name is in use. Please enter another.'
                        create_account()
                    elif new_account_username not in account_holders and new_account_username != '*':
                        new_account_password = raw_input('Please create a password for ' + new_account_username + ': ')
                        if new_account_password == '*':
                            menu()
                        else:
                            new_account_opening_balance = raw_input('Opening balance: ')
                            if new_account_opening_balance == '*':
                                menu()
                            else:
                                users[new_account_username] = new_account_password
                                account_holders[new_account_username] = int(new_account_opening_balance)
                                print 'An account has been created for ' + new_account_username + ' with starting balance of ' + new_account_opening_balance
                                menu1_f_a()
                    elif new_account_username == '*':
                        menu()

                create_account()

            ##3
            elif int(islem2) == 3:
                print '===== Admin: Close Account ====='

                def close_account():
                    close_account_username = raw_input('Please enter account holder name: ')
                    if close_account_username not in account_holders and close_account_username != '*':#check if the entered acoount is exist
                        print 'There is no available account for this account holder.\nYou may try again with another name.'
                        close_account()
                    elif close_account_username in account_holders:
                        close_account_onay = raw_input(
                            'The account for customer ' + close_account_username + ' will be closed.\nDo you approve (yes/no?): ')#asking for approve
                        if close_account_onay == 'yes':
                            users.__delitem__(close_account_username)#deletes the acoount from users dict.
                            account_holders.__delitem__(close_account_username)#deletes the acoount from acoount holders dict.
                            print 'The account for customer ' + close_account_username + ' closed.'
                            menu1_f_a()
                        elif close_account_onay == 'no':
                            print 'Your account closing request has been canceled.'
                            menu1_f_a()
                        elif close_account_onay == '*':
                            menu()
                    elif close_account_username == '*':
                        menu()

                close_account()
            ##4
            elif int(islem2) == 4:
                print '===== Admin: Search for an Account ====='

                def search_account():
                    search_account_username = raw_input('Please enter account holder name: ')
                    if search_account_username not in account_holders and search_account_username != '*':#check if the entered acoount is exist
                        print 'There is no available account for this account holder.\nYou may try again with another name.'
                        search_account()
                    elif search_account_username in account_holders:
                        print 'Account Holder: ' + search_account_username + '\nCurrent Balance: ' + str(
                            account_holders[search_account_username]) + ' TL'
                        menu1_f_a()#running the menu1_f_a function
                    elif search_account_username == '*':#secret code
                        menu()#running the menu function

                search_account()#running the search_account function
            ##5
            elif int(islem2) == 5:
                print '===== Admin: See the Stats ====='#greetings
                count0 = 0
                #takes values one by one
                for i in account_holders:
                    if account_holders[i] > 0:
                        count0 += 1
                count1 = 0
                for j in account_holders:
                    count1 += account_holders[j]
                #prints the stats
                print 'Total Number of Accounts: ' + str(len(account_holders))
                print 'Number of Accounts with Non-Zero Balance: ' + str(count0)
                print 'Total Balance: ' + str(count1) + ' TL'
                print 'Average Balance: ' + str(round(float((count1) / float(len(account_holders))), 2)) + ' TL'
                menu1_f_a()

            ##6
            elif int(islem2) == 6:#goes to main menu
                menu()#running the menu function

        admin_login()#running the admin_login function
    # 9
    elif int(islem0) == 9:#if the entry is 9, program terminates it self
        print 'Program Terminated !'


login()#running the login function
