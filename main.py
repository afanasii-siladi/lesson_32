from operation_math import add, sub, mul, div

while True:
    next_cal = input('Let is do next calculation, yes or no?\n')
    if next_cal == 'no':
        break
    print('Select operation -> 1 - add or 2 - subtract or 3 - multiply or 4 - divide')
    operation = input('Write down the number(1, 2, 3 or 4 --> )')

    if operation not in ('1', '2', '3', '4'):
        print('Error')
        
    else:
        for i in range(1):
            num = int(input('Enter number --> '))
            num2 = int(input('Enter number --> '))

    if operation == '1':
        print(num, '+', num2, '=', add(num, num2))
    elif operation == '2':
        print(num, '-', num2, '=', sub(num, num2))
    elif operation == '3':
        print(num, '*', num2, '=', mul(num, num2))
    elif operation == '4':
        print(num, '/', num2, '=', div(num, num2))