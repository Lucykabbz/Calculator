firstnumber = float(input("Enter first number:"))
secondnumber = float(input("Enter second number:"))
myoperator = str(input("Enter the operator: (+, -, *, /)"))

if myoperator == "+":
    print(firstnumber + secondnumber)
elif myoperator == "-":
    print(firstnumber - secondnumber)
elif myoperator == "*":
    print(firstnumber * secondnumber)
elif myoperator == "/":
    print(firstnumber / secondnumber)
else:
    print("Not applicable")
