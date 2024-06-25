# Customer Banking Interface

## Description

This script lets you calculate your interest for both a savings account and a CD account. 

This is the first step into object oriented programming for me. The Account.py file creates the Account class and creates methods to set the parameters necessary for the class.
The savings_account.py file imports the Account class from Account.py and uses it and its methods to create a function that can take necessary parameters to create an Account class object for a savings account and calculate the amount of interest gained. 
The cd_account.py does the exact same thing as its savings counterpart, but for a cd account.
The customer_banking.py imports the functions within the two aformentioned files containing functions for creating accounts, takes inputs from the user, and applies those inputs to the account creating functions in order to create accounts and perform interest calculations. All of this is contained within the main function, which additionally prints the updated balances and interest gained over time for respectively for accounts created. 

## How to Use

**Run the Script**: Execute the script to start the ordering process.

**Enter your Savings Account Information**: Choose a category from Snacks, Meals, Drinks, or Desserts by typing the corresponding number.

1. ***Select an Item***: Within the chosen category, select an item by typing its number.

2. ***Specify Quantity***: Enter the desired quantity of the selected item.

3. ***Continue or Complete Order***: Decide whether to continue ordering or to complete the order.

**Review Order**: Once the order is complete, the script will display a summary of all items ordered along with their prices and quantities, and calculate the total cost.

