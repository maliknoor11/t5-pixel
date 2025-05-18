num1 = 0
num2 = 0
result = 0
operation = None 


num1 = int(input("Enter the first number: "))
num2 = int(input( "Enter the second number: "))
operation = input("Choose an operation +, -, /, *" )

if operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print (result)