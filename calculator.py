
# a function to add two numbers and return their addition  
def add(n1, n2) -> float:
    return n1 + n2

# a function to subtract number n2 from n2
def subtract(n1, n2) -> float:
    return n1 - n2

# a function to multiply two numbers and return their multiplication
def multiply(n1, n2) -> float:
    return n1 * n2

#a function to divide a float n1 by n2
def divide(n1, n2) -> float:
    return float(n1)/n2

if __name__ == "main":
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter the second number: "))
    except ValueError:
        print("Enter number only!!")

    print("Enter:1 \n1 for addition, \n2 for subtraction, \n3 for multiplication and \n4 for division")
    operation = int(input("Enter the number of operation:"))
    if (operation == 1):
        print(add(n1, n2))
    elif(operation == 2):
        print((subtract(n1, n2)))
    elif(operation == 3):
        print(multiply(n1, n2))
    elif(operation == 4):
        print(divide(n1, n2))
    else:
        print("Only enter numbers between 1-4")
