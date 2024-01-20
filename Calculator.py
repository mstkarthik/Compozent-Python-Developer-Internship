# Basic Task
#1. Calculator: Create a basic calculator that performs operations like addition, subtraction, multiplication, and division.

#functions that calculates
def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiplication(num1 , num2):
  return num1 * num2

def division(num1 , num2):
  return num1/num2

print("---Please enter the choice---")
print("enter 1 for addition")
print("enter 2 for subtraction")
print("enter 3 for multiplication")
print("enter 4 for division")

#while loop allows users to perform multiple calculation
while(True):
  ch = int(input("your choice is: "))

  if ch in [1,2,3,4]: #if checks whether choice is present or not
    try:
      num1 = float(input("Enter your first number: "))
      num2 = float(input("Enter your second number: "))

    except Exception as e: # except block catches the error such as ZerodivisionError or so.
      print("error is: ", e)
      continue

#if and elif statement will call and get the function returned value which the answer
    if(ch == 1):
      print("The addition of: ", num1," and ",num2, " is ", addition(num1,num2))

    elif(ch == 2):
      print("The subtraction of: ", num1," and ",num2, " is ", subtraction(num1,num2))

    elif(ch == 3):
      print("The multiplication of: ", num1," and ",num2, " is ", multiplication(num1,num2))

    elif(ch == 4):
      print("The division of: ", num1," and ",num2, " is ", division(num1,num2))

#this if will break the while loop
    next_cal = input("would you like to calculate further yes or no\n")
    if(next_cal.lower() == "no"):
      break

#this else will only get printed if choice is not 1,2,3 or 4
  else:
    print("invalid input")
