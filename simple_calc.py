def calculate(expression):
    try:
        result = eval(expression)
        if result == float('inf') or result == float('-inf'):
            raise ValueError("Division by infinity")
    except ZeroDivisionError:
        result = float('inf')
    except ValueError as e:
        result = None
        print("Error:", e)
    except:
        result = None
        print("Error: invalid expression")
    return result

def is_valid_expression(expression):
    valid_chars = "0123456789+-*/() "
    for char in expression:
        if char not in valid_chars:
            return False
    return True

while True:
    end_expressions = ["exite", "end", "q", "quite"]
    expression = input("Enter a mathematical expression: ")
    if expression in end_expressions:
        break
    if is_valid_expression(expression):
        result = calculate(expression)
        if result is not None:
            print("Result:", result)
    else:
        print("Invalid expression")