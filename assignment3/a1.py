#2.Write a Python function called calculator that takes three arguments:
# num1 (float), num2 (float), and operation (string). The function should 
# perform the specified operation ('add', 'subtract', 'multiply', 'divide') 
# on num1 and num2 and return the result



num1=int(input("value of number one:"))
num2=float(input("value of number two:"))
operation=str(input("input what operation do you want===  "))


if operation == 'add':
    
    
    addition=num1+num2
    
    print("addition is",addition)
elif operation == 'sub':
    
    subtration= num1 - num2
    print("subtration is :",subtration)
elif operation == 'mul':
    
    multiply= num1 * num2
    print("multiply is:",multiply)
elif operation == 'divide':
    
    if num2 == 0:
        print("Error: Division by zero")
    else:
        
        divide=num1 / num2
        print("division is:",divide)
        
else:
    
        
    print("Error: Invalid operation")

