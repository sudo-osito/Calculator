# Calculator

from pickle import STOP


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("--------------------------------")
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("--------------------------------")

    choice = int(input("Enter your choice: "))
    print("--------------------------------")

    if choice == 1:
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("--------------------------------")
        print(f"Result: {add(a, b)}")
        print("Do you want to continue? (y/n)")
        if input() == "y":
            main()
        else:
            return print("Exiting...")

    elif choice == 2:
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("--------------------------------")
        print(f"Result: {subtract(a, b)}")
        print("Do you want to continue? (y/n)")
        if input() == "y":
            main()
        else:
            return print("Exiting...")

    elif choice == 3:
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("--------------------------------")
        print(f"Result: {multiply(a, b)}")
        print("Do you want to continue? (y/n)")
        if input() == "y":
            main()
        else:
            return print("Exiting...")

    elif choice == 4:
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("--------------------------------")
        print(f"Result: {divide(a, b)}")
        print("Do you want to continue? (y/n)")
        if input() == "y":
            main()
        else:
            return print("Exiting...")
            
    elif choice == 5:
        return print("Exiting...")
          
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()