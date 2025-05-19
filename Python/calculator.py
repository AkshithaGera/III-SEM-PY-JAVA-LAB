print("***** Simple Caluculator *****")

num1 = input("Enter the first value : ")
num2 = input("Enter the second value : ")
operator = input("Choose the operator (+, -, *, /): ")

if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
    num1 = float(num1)
    num2 = float(num2)
    if operator == '+':
        print(f"The Result {num1} + {num2} is : {num1+num2}")
    elif operator == '-':
        print(f"The Result {num1} - {num2} is : {num1-num2}")
    elif operator == '*':
        print(f"The Result {num1} * {num2} is : {num1*num2}")
    elif operator == '/':
        if num2 != 0:
            print(f"The Result {num1} / {num2} is : {num1/num2}")
        else:
            print("We cann't do this operation with denominator 0")
    else:
        print("Please select the operators mentioned above.")
else:
    print("Invalid Choice of numbers !!! Please give me the digits .")
