import random


cash = 10

balance = 0
a = 0.5
b = 1.7

stock1 = 2
stock2 = 5
stock3 = 10
ystock1 = 0
ystock2 = 0
ystock3 = 0
yindexfund = 0



x = 0
interest_rate = 1.2
while x == 0:
    interestmult = interest_rate/100 + 1
    balance = balance*interestmult
    figure1 = random.uniform(a,b)
    figure2 = random.uniform(a,b)
    figure3 = random.uniform(a,b)
    stock1 = stock1*figure1
    stock2 = stock2*figure2
    stock3 = stock3*figure3

    cash4 = cash/4
    cash2 = cash/2
    cash34 = 3*cash/4
    balance4 = balance/4
    balance2 = balance/2
    balance34 = 3*balance/4



    indexfund = stock1 + stock2 + stock3 + 100
    vystock1 = ystock1*stock1
    vystock2 = ystock2*stock2
    vystock3 = ystock3*stock3
    vyindexfund = yindexfund*indexfund
    vstock = vystock1 + vystock2 + vystock3 + vyindexfund
    value = balance + cash + vstock
    print(" ")


    response = input("Welcome to the Federal Reserve Banking Game. What action would you like to do? To see current balance, type Balance. To withdraw money, type Withdraw. To deposit money, type Deposit. To re-nagotiate you interest rate, type Interest. To buy stock, type Stock. To sell stock, type Sell. To talk with a teller, please type Teller. To exit, type Exit. Please mind the capitol letters. ")
    print(" ")
    if response == "Balance":
        print(f"Your balance is {balance}. You have {cash} cash on hand. Your interest rate is {interest_rate}%. Your stock value is {vstock}. Your net worth is {value}. ")
    elif response == "Withdraw":
        withdraw = input(f"Would you like to withdraw {balance4}, {balance2}, or {balance34}? Type 1, 2, or 3. ")
        if withdraw == "1":
            balance = balance - balance4
            cash = cash + balance4
            print(f"Your current balance is {balance}. You have {cash} on hand.")
        elif withdraw == "2":
            balance = balance - balance2
            cash = cash + balance2
            print(f"Your current balance is {balance}. You have {cash} on hand.")
        elif withdraw == "3":
            balance = balance - balance34
            cash = cash + balance34
            print(f"Your current balance is {balance}. You have {cash} on hand.")
    elif response == "Deposit":
        deposit = input(f"Would you like to deposit {cash4}, {cash2}, or {cash34}? Type 1, 2, or 3. ")
        if deposit == "1":
            balance = balance + cash4
            cash = cash - cash4
            print(f"Your current balance is {balance}. You have {cash} on hand.")
        elif deposit == "2":
            balance = balance + cash2
            cash = cash - cash2
            print(f"Your current balance is {balance}. You have {cash} on hand.")
        elif deposit == "3":
            balance = balance + cash34
            cash = cash - cash34
            print(f"Your current balance is {balance}. You have {cash} on hand.")
    elif response == "Interest":
        interest = input(f"Your current rate is {interest_rate}. Our options are for $7000, increase rate by 2%. For $30000, increase rate by 5%. For $50000, increase rate by 7%. Type 1, 2, or 3. ")
        if interest == "1":
            if balance - 7000 < 0:
                print("Please talk to teller.")
            else:
                interest_rate = interest_rate + 2
                balance = balance - 7000
                print(f"Your new interest rate is {interest_rate}.")
        elif interest == "2":
            if balance - 30000 < 0:
                print("Please talk to teller.")
            else:
                interest_rate = interest_rate + 5
                balance = balance - 30000
                print(f"Your new interest rate is {interest_rate}.")
        elif interest == "3":
            if balance - 50000 < 0:
                print("Please talk to teller.")
            else:
                interest_rate = interest_rate + 7
                balance = balance - 50000
                print(f"Your new interest rate is {interest_rate}.")

    elif response == "Teller":
        print("Unfortunatly, due to the Goverment Shutdown, our tellers are unavaible. We are sorry for the inconvinence. If you require sirvice, please either visit the bank in person or call us. Our phone number is located on our website.")
    elif response == "Stock":
        stock = input(f"We have several stocks avalible for purchase. To buy stock 1, valued at {stock1}, type Stock1. To buy stock 2, valued at {stock2}, type Stock2. To buy stock 3, valued at {stock3}, type Stock3. To buy one share of index fund, valued at {indexfund}, type Index Fund. To buy 5 shares of Index Fund, type 5. ")
        if stock == "Stock1":
            if cash - stock1 < 0:
                print("Please talk to teller.")
            else:
                cash = cash - stock1
                ystock1 = ystock1 + 1
        elif stock == "Stock2":
            if cash - stock2 < 0:
                print("Please talk to teller.")
            else:
                cash = cash - stock2
                ystock2 = ystock2 + 1
        elif stock == "Stock3":
            if cash - stock3 < 0:
                print("Please talk to teller.")
            else:
                cash = cash - stock3
                ystock3 = ystock3 + 1
        elif stock == "Index Fund":
            if cash - indexfund < 0:
                print("Please talk to teller.")
            else:
                cash = cash - indexfund
                yindexfund = yindexfund + 1
        elif stock == "5":
            if cash - indexfund*5 <0:
                print("Please talk to teller.")
            else:
                cash = cash - indexfund*5
                yindexfund = yindexfund + 5
        print(f"Thanks for buying {stock}.")
    elif response == "Sell":
        sell = input(f"You have {ystock1} shares of Stock 1, {ystock2} shares of Stock 2, {ystock3} shares of Stock 3 and {yindexfund} shares of Index Fund. Which one do you want to sell? ")
        if sell == "Stock 1":
            if ystock1 <= 0:
                print("Please talk to teller.")
            ystock1 = ystock1 - 1
            cash = cash + stock1
        if sell == "Stock 2":
            if ystock2 <= 0:
                print("Please talk to teller.")
            ystock2 = ystock2 - 1
            cash = cash + stock2
        if sell == "Stock 3":
            if ystock3 <= 0:
                print("Please talk to teller.")
            ystock3 = ystock3 - 1
            cash = cash + stock3
        if sell == "Index Fund":
            if indexfund <= 0:
                print("Please talk to teller.")
            indexfund = indexfund - 1
            cash = cash + indexfund
    elif response == "Exit":
        print(f"Thank you for visiting the Federal Reserve Bank. Your final net worth is {value}. Please come again.")
        x = 1
    if value >= 10000000:
        print("Congradulations! You have beaten the game!")
        print(f"Your balance is {balance}. You have {cash} cash on hand. Your interest rate is {interest_rate}%. Your stock value is {vstock}. Your net worth is {value}. The final values of the stocks are {stock1}, {stock2}, {stock3}, and {indexfund}. ")
        x = 1


        


