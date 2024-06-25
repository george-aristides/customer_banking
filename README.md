# Customer Banking Interface

## Description

This script lets you calculate your interest for both a savings account and a CD account. 

- This is the first step into object oriented programming for me. The Account.py file creates the Account class and creates methods to set the parameters necessary for the class.

- The savings_account.py file imports the Account class from Account.py and uses it and its methods to create a function that can take necessary parameters to create an Account class object for a savings account and calculate the amount of interest gained. 

- The cd_account.py does the exact same thing as its savings counterpart, but for a cd account.

- The customer_banking.py imports the functions within the two aformentioned files containing functions for creating accounts, takes inputs from the user, and applies those inputs to the account creating functions in order to create accounts and perform interest calculations. All of this is contained within the main function, which additionally prints the updated balances and interest gained over time for respectively for accounts created. 

## How to Use

**Run the Script**: Execute the script to start the process.

**Enter your Savings Account Information**: You will receive a series of prompts for the necessary parameters.

1. ***Balance***: Enter the initial balance of your savings account.

2. ***Interest Rate***: Enter the interest rate, as a percentage. For example, if you receive 5.5% interest, enter 5.5. The script will automatically convert it to a decimal, so do not enter "0.055" for 5.5%! 

3. ***Length of Term***: Enter the number of months you will be receiving interest over. Keep this a whole number of months only. Do not use fractions of months like "6.5", and do not try to use days, weeks, years, or any other unit of time.

**Repeat for CD Account**: Follow the same set of steps for your CD Account! The program will print out your updated balance and interest earned for each account individually after receiving all necessary information for each respective account. 
