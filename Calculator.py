n1 = float(input("Enter first  operator: "))
n2 = float(input("Enter second operator: "))
opt = input("Enter the operand(+,-,*,/) to perform the operation on operator: ")
if (opt=='+'):
  res = n1+n2
  print("Addition of n1 and n2 is: ",res)
elif (opt == '-'):
  res = n1-n2
  print("Substraction of n1 and n2 is: ",res)
elif (opt == '*'):
  res = n1*n2
  print("Multiplication of n1 and n2 is: ",res)
elif (opt == '/'):
  if(n2==0):
    print("Division by zero is not possible")
  else:
    res = n1/n2
    print("Division of n1 and n2 is: ",res)
