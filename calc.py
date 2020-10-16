#calculator


#addition
def add(x,y):
    return x + y

#subtraction
def sub(x,y):
    return x - y

#multiplication
def mul(x,y):
    return x * y

#division
def div(x,y):
    return x / y
print ("This is calculator")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice = input("choose from the options (1, 2, 3, 4): ")

num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
if choice =='1':
    print(f'{num1} + {num2} = {add(num1, num2)}')
if choice == '2':
    print(f'{num1} - {num2} = {sub(num1, num2)}')
if choice =='3':
    print(f'{num1} * {num2} = {mul(num1, num2)}')
if choice =='4':
    print(f'{num1} / {num2} = {div(num1, num2)}')

number = 35
if number > 30:
 print("it is greater than")
 print("it is less than")
elif number > 20:
    print ("its equal")
else:
 print ("its normal")
print ("Done")

age = 22
message = "eligible" if age >= 18 else "Not eligible"
print(message)


