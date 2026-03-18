'''
Assignment 4
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''
# Math Library needs to be imported first #
import math

# prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2) #
'''
I did this at first but it was wrong
point1 = float(input("Enter the first point: "))
point2 = float(input("Enter the second point: "))

x1, y1 = point1
x2, y2 = point2

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
'''

x1 = float(input("Enter the first point: "))
y1 = float(input("Enter the first point: "))
x2 = float(input("Enter the second point: "))
y2 = float(input("Enter the second point: "))

# calcuation is provided above but you cannot use ^ and need to replace with two * #
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print ("distance between the two points: ", distance)






