"""
Last assignment I included a lot of these docstrings with detailed explanations
as to what the code does etc. because there was a lot of book keeping to be
done with that assignment.

For this one I feel like the actual code is very minimal and clearly defined by 
the instruction comments thus I am not going to include these docstrings to 
describe everything in detail.
"""


# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("What is your savings balance: "))
    savings_interest = float(input("What is your savings interest rate: "))
    savings_maturity = int(input("How many months have are you saving: ")) # months?
    # Call the create_savings_account function and pass the variables from the user.
    savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated balance with savings is : ${savings_balance}.") 
    print(f"Interest earned over {savings_maturity} months is {interest_earned}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("What is your CD balance: "))
    cd_interest = float(input("What is your CD interest rate: "))
    cd_maturity = int(input("How many months: ")) # months?

    # Call the create_cd_account function and pass the variables from the user.
    cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated balance with savings is : ${cd_balance}.") 
    print(f"Interest earned over {cd_maturity} months is {interest_earned}")

if __name__ == "__main__":
    # Call the main function.
    main()