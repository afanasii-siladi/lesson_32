while True:
    try:
        a = float(input("number --> "))
    except:
        print('Error in 1st input')
        quit()
    try:    
        q = float(input("number --> "))
    except:
        print('Error in 2nd input')
        quit()

    b = input("+,-,* or / --> ")

    if b == '+':
        c = a+q
    elif b == '-':
        c = a-q    
    elif b == '*':
        c = a*q    
    else:
        try:
            c = a/q  
        except ZeroDivisionError:
            print('Division by zero error')    
    print(c)