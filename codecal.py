first = float(input("Enter value: "))

while True:
    print("+, -, /, *, %, =")
    op = input('Enter Operator: ')

    if op == '=':
        break

    next = float(input('Enter Next Value: '))

    if op == '+':
        first = first + next
    elif op == '-':
        first = first - next
    elif op == '/':
        if next == 0:
            print("Math Error")
            continue
        else:
            first = first / next
    elif op == '*':
        first = first * next
    elif op == '%':
        first = first % next
    else:
        print("Invalid Operator")
        continue

    print("Current Answer:", first)

print("Final Answer:", first)
