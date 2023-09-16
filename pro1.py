import math
print("Select option.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Sine")
print("6. Cosine")
print("7. Tangent")
print("8. Square root")
print("9. Exponential")
print("10. LogBase10")
print("11. Power")
print("12. Square Root")

# Please Select options between 1-12
choice = input("Please Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12): ")

if choice in ('1', '2', '3', '4', '11'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", num1 + num2)

    elif choice == '2':
        print(num1, "-", num2, "=", num1 - num2)

    elif choice == '3':
        print(num1, "*", num2, "=", num1 * num2)

    elif choice == '4':
        print(num1, "/", num2, "=", num1 / num2)

    elif choice == '11':
        print(num1, "", num2, "=", num1 ** num2)


elif choice in ('5', '6', '7', '8', '9', '10', '12'):
    num = float(input("Enter a number: "))

    if choice == '5':
        print("sin(", num, ") =", math.sin(num))

    elif choice == '6':
        print("cos(", num, ") =", math.cos(num))

    elif choice == '7':
        print("tan(", num, ") =", math.tan(num))

    elif choice == '8':
        print("sqrt(", num, ") =", math.sqrt(num))

    elif choice == '9':
        print("exp(", num, ") =", math.exp(num))

    elif choice == '10':
        print("log(", num, ") =", math.log(num))

    elif choice == '12':
        print(num, " ", "0.5", "=", num ** 0.5)

else:
    print("Invalid Input ! Please Enter between 1-12 ")