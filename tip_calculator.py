'''
Assignment 1: Tip Calculator
Author: J-bell0
Additional information: Written for python 3

'''

#1. Get the user input (total bill amount)
bill_amount = input("Enter the Bill amount? ")

#1.1 Error handling
while True:
    try: 
        bill_amount = float(bill_amount)
        break 
    except ValueError: 
        print()
        print("Your entry is invalid :(", "Please enter a numeric value")
        bill_amount = (input("what is the total bill amount? "))
        
#2 Recommended tip amounts (%)
tip_percent  = [15, 18, 20] 
print()                                                            # List to store tip percentages
print("The recommended tip amounts are 15%, 18%, and 20%")

#2.2 Error handling; check for valid user-inputs
tip_level = input("Type '1', '2', or '3' to select a tip percentage: ")                 # Get the tip level from the customer
while True:                                                                             # check that the user input is a numeric value
    try: 
        tip_level = int(tip_level)                                                      # convert user-input from string to integer
        while tip_level not in range(1,4):                                              # Check that the user-input is between 1 and 3
            print()                                                             
            print("Please select either '1', '2' or '3' to make a selection")
            tip_level = input("Type '1', '2', or '3' to select a tip percentage: ")
            tip_level = int(tip_level)
        else:
            break 
    except ValueError: 
        print()
        print("Your entry is invalid :(", "Please enter a numeric value")
        tip_level = input("Type '1', '2', or '3' to select a tip percentage: ")
        
#3 Generate the payment summary for each tip selected
print()
print(f"You have selected the {tip_percent[tip_level-1]}% tip amount")
tip_amount = ((tip_percent[tip_level-1]/100) * bill_amount)
print()
print("                    --Payment Summary--                        ")
print("---------------------------------------------------------------")
print(f"Your Tip amount is: ${tip_amount:0.2f}")
print(f"Your Bill amount is: ${bill_amount}")
total_bill_amount = tip_amount+ bill_amount
print(f"Your Total bill amount (plus tip) is: ${total_bill_amount}")
print("---------------------------------------------------------------")
print("              --Thank you for your patronage--                 ")
print()