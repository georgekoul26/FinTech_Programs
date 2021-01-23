#This is a simple program that can recommend whether to buy or sell a stock based on an the percent change of the stock(20% selected arbitrarily).  The program can also check your balance and verify that you have sufficient funds to complete the trade. 




#Create recommendation function which calculates the percent difference and provides a recommendation on whether to buy/sell/hold

def recommend():
    original_price = float(input("Original Price:"))
    current_price = float(input("Current Price:"))
    balance = float(input("Account Balance:"))
    threshold_to_buy = -20
    threshold_to_sell = 20
    difference = current_price - original_price
    percent_difference = difference / original_price * 100
    if percent_difference >= threshold_to_sell:
        balance += current_price
        recommendation = "Sell"
    elif percent_difference <= threshold_to_buy:
        if balance >= current_price:
            balance -= current_price
            recommendation = "Buy"
        else: print ("Insufficient funds")
    else: recommendation = "Hold"
    print (recommendation)
    return recommendation, balance, current_price

#Request number of shares to buy/sell and define execute function to execute trade and print new "share quantity" and "account balance"


def execute():
    recommendation, current_price, balance = recommend()
    shares_owned = int(input("Number of shares owned:"))
    if recommendation == "Sell": 
        sell_order_quantitiy = int(input("How many shares do you want to sell?"))
        if sell_order_quantitiy > shares_owned:
            print ("You do not own that many shares.  Let's try again.")
            print ("How many shares do you want to sell?")
        elif sell_order_quantitiy < 0:
            print ("This input is not valid.  Let's try again.")
            print ("How many shares do you want to sell?")
        elif sell_order_quantitiy == 0:
            print ("Confirmed.  You want to hold your position.")
        else:
            balance += sell_order_quantitiy * current_price
            new_shares_owned = shares_owned - sell_order_quantitiy
            print (f"Your new balance is ${balance}")
            print (f"Your now own {new_shares_owned} shares.")
    if recommendation == "Buy":
        buy_order_quantitiy = int(input("How many shares do you want to buy?"))
        if buy_order_quantitiy * current_price > balance:
            print ("You have and inadequate balance for that purchase.  Let's try again.")
            print ("How many shares do you want to buy?")
        else: print ("Placeholder")

#Call functions using main function

def main():
    execute()

if __name__ == "__main__":
    main()

#To do 1.21.21:
    #1) Find a way to make out of range answers repeat the question.  IDEA: use a while loop
    #2) Complete the Buy recommendation branch of the execute function
    #3) Upload to Github so that I can try different methods to expand script
    #4) Potential expansions: Add branch to execute function allowing to confirm trade before execution