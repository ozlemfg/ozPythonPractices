# ********* Functions to calculate****
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b

while True:

    try:
        op = int(input("select your operation: 1-Add, 2-Sub, 3-Mul, 4-Div : "))
    except ValueError:
         print("enter digital value")
         continue

    if op not in range(1, 5):
        print("Enter between 1 and 4")
        continue

    try:
        x = int(input("enter your first number: "))
        y = int(input("enter your second number: "))
    except ValueError:
        print("provide numbers-")
        continue

    if op == 1:
             print(x, "+", y, "=", add(x, y))

    elif op == 2:
             print(x, "-", y, "=", sub(x, y))

    elif op == 3:
             print(x, "x", y, "=", mul(x, y))

    elif op == 4:
        if y == 0:
            print("cannot divide by 0 ")
        else:
            print(x, "/", y, "=", div(x, y))
    break
