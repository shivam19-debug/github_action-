def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("--- Simple Python Calculator ---")
    print("Operations: +, -, *, /")
    
    while True:
        num1_input = input("\nEnter first number (or 'q' to quit): ").strip()
        if num1_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            num1 = float(num1_input)
            operator = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")
            continue

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator selected.")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
