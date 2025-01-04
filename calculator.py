import math


version = 'Calculator 1.3'


print("\nHello World! \n"
      f"Running {version}")


startup = '2'

while startup != '1':
    startup = input("\n\nStart Calculator?\n"
                    "\n1: Yes"
                    "\n2: No"
                    "\n\nAnswer here: ")


while True:
    try:
        x = float(input("\nEnter your first number (X): "))
        break
    except ValueError:
        print("\nInvalid input. Enter a numeric Value.")

while True:
    try:
        y = float(input("Enter your second number (Y): "))
        break
    except ValueError:
        print("\nInvalid input. Enter a numeric Value.\n")


op = 'n/a'

while op not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
     op = input(f"\n\nSelect Operation"
                "\n1: (X + Y) Addition"
                "\n2: (X - Y) Subtraction"
                "\n3: (X x Y) Multiplication"
                "\n4: (X / Y) Division"
                "\n5: (X ^ Y) Indicy"
                "\n6: (X ^ 2) Square Root"
                "\n7: (sin(x) cos(x) tan(x)) Trigonometery"
                "\n8: (X\u2081\u2080 -> X\u2082) Convert Denary to Binary, decimals will be rounded."
                "\n9: (X\u2081\u2080 -> X\u2081\u2086) Convert Denary to Hexadecimal, decimals will be rounded."
                "\n\nAnswer Here: ")


if op == '1':
     answer = x + y
     print(f"\n\nThe answer to {x} + {y} is: ", end="")

if op == '2':
     answer = x - y
     print(f"\n\nThe answer to {x} - {y} is: ", end="")

if op == '3':
     answer = x * y
     print(f"\n\nThe answer to {x} x {y} is: ", end="")

if op == '4':
     answer = x / y
     print(f"\n\nThe answer to {x} / {y} is: ", end="")

if op == '5':
     answer = x ^ y
     print(f"\n\nThe answer to {x} ^ {y} is: ", end="")

if op == '6':
     answer = math.sqrt(x)
     print(f"\n\nThe answer to {x} ^ 1/{y} is: ", end="")


trig = '0'

if op == '7':
     while trig not in ['1', '2', '3']:
          trig = input("\n\n1: Sine"
                       "\n2: Cosine"
                       "\n3: Tangent"
                       "\n\nAnswer here: ")
     if trig == '1':
          answer = math.sin(x)
          print(f"\n\nThe answer to sin({x}) is: ", end="")

     if trig == '2':
          answer = math.cos(x)
          print(f"\n\nThe answer to cos({x}) is: ", end="")

     if trig == '3':
          answer = math.tan(x)
          print(f"\n\nThe answer to tan({x}) is: ", end="")


if op == '8':
     answer = format(int(round(x)), 'b')
     print(f"\n\n{x} converted into Binary is: {x} \u2081\u2080 -> {answer} \u2082", end="\n")


if op == '9':
     answer = format(int(round(x)), 'x')
     print(F"\n\n{x} converted into Hexadeciaml is: {x} \u2081\u2080 -> {answer} \u2081\u2086", end="\n")     


if op in ['1', '2', '3', '4', '5', '6', '7']:
     print(f"{answer:,}\n")

if op in ['1', '2', '3', '4', '5', '6', '7']:
     round = '0'
     while round not in ['1', '2']:
          round = input("Would you like to round your answer?\n1: Yes\n2: No\n\nAnswer here: ")

     if round == '1':
          dp = int(input("\n\nTo how many decimal places? (1, 2, 3...)\n\nAnswer here: "))
          round(answer, ndigits=dp)
          print(f"\nYour rounded answer is {answer}\n")
     else:
          print(f"\nYour answer is {answer}\n")