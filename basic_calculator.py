def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def mul(a, b):
    c = a * b
    return c

def div(a, b):
    return a / b

def rem(a, b):
    return a % b

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder\n"))

if c == 1:
    result = add(a, b)
    print("Result:", result)

if c == 2:
    result = sub(a, b)
    print("Result:", result)

if c == 3:
    result = mul(a, b)
    print("Result:", result)

if c == 4:
    result = div(a, b)
    print("Result:", result)

if c == 5:
    result = rem(a, b)
    print("Result:", result)
