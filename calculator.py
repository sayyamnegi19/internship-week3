class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except Exception as e:
            print(f"Error: {e}")

    def subtract(self, a, b):
        try:
            return a - b
        except Exception as e:
            print(f"Error: {e}")

    def multiply(self, a, b):
        try:
            return a * b
        except Exception as e:
            print(f"Error: {e}")

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    calc = Calculator()

    print("Addition:", calc.add(10, 5))
    print("Subtraction:", calc.subtract(10, 5))
    print("Multiplication:", calc.multiply(10, 5))
    print("Division:", calc.divide(10, 5))

    result = calc.divide(10, 0)
    if result is not None:
        print("Division:", result)
