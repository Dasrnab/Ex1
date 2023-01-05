#taking two inputs and Sign

Num1 = float(input("Please enter your 1st number "))
Sign = input("Please enter '*' , '+', '-', '/' ")
Num2 = float(input("Please enter your 2nd number "))
Nothing = "No Calculation"

if Sign == '*':
  Mul = Num1 * Num2
  print(f'The multiplication of two numbers is {Mul}')
elif Sign == '+':
  Sum = Num1 + Num2
  print (f'The sum of two numbers is {Sum}')
elif Sign == '-':
  Sub = Num1 - Num2
  print(f' The subtration of two number is {Sub}')
elif Sign == '/':
  Div = Num1 / Num2
  print(f' The division of two numbers is {Div}')
else:
 print(Nothing)
