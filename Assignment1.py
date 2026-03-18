
'''

Assignment 1
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.

=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''

# Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years) below #

principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the interest rate: ")) - this came up and thought I would keep it top remind me #
rate_input = input("Enter the interest rate: ")
rate = float(rate_input)
time = float(input("Enter the time period: "))

# calculate the simple interest using this formula Principal * Rate * Time #
simple_interest = principal*rate*time/100

# display output below #

print()
print("Simple Interest: ", simple_interest)

# How do I get two decimal places to show in my output? #

