#!/usr/bin/python3
#Name: Calculator3
#Program purpose: A program to be used as a calculator 
#Author: Stephano G.
#Date: June 5, 2022 
#Version: 3.0 
#Completion time: 1 hour

#Function for outputting and receiving menu options
def show_menu():
    print("Menu options:")
    print("  +: to add")
    print("  -: to subtract")
    print("  *: to multiply")
    print("  /: to divide")
    print("")
    print("")
    
#function to prompt for a number
def get_float(prompt): 
    return float(input(prompt))

#Addition function
def add(num1, num2):
    return num1 + num2

#Subtraction function
def subtract(num1, num2):
    return num1 - num2

#Multiplication function
def multiply(num1, num2):
    return num1 * num2

#Division function
def divide(num1, num2):
    return num1 / num2

#Function to check if the divisor is 0
def iszero(num2):
    if (num2 == 0) or (num2 == 0.0):
        return True 
    else:
        return False


#main function
def main():
    show_menu()
    operator = input("Enter operator (q to quit): ").upper()
    while operator != "Q":

#Asking for user input 
        num1 = get_float("Enter first number: ") 
        num2 = get_float("Enter second number: ") 

#Addition
        if operator == "+":
            summ = add(num1,num2)
            prompt = print("-> Result of the calculation: " + str(summ))

#subtraction
        elif operator == "-":
            sub = subtract(num1,num2)
            prompt = print("-> Result of the calculation: " + str(sub))
#Multiplication
        elif operator == "*":
            multi = multiply(num1,num2)
            prompt = print("-> Result of the calculation: " + str(multi))

#Division
        elif operator == "/":
#Error checking for divisor
            while iszero(num2):
                print("Division by zero cannot be performed.") 
                num2 = get_float("Enter a non-zero divisor: ") 
            div = divide(num1,num2)
            prompt = print("-> Result of the calculation: " + str(div))
        
#Reprompt for an operator   
        show_menu() 
        operator = input("Enter operator (q to quit): ").upper()

#Calling of main function
main()




