'''
Assignment 3
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
'''

# Prompt the user to enter their weight in kg and height in meters #

weight = float(input("Enter the weight in kilograms: "))
height = float(input("Enter the height in meters: "))

# Calculate the BMI using the formula: BMI = Weight / (Height^2) #

bmi = weight / (height ** 2)

# show user their BMI #

print("BMI is", bmi)

