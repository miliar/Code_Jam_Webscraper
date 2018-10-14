#!/usr/bin/python
        
def pres(case, value):
    print("Case #" + str(case) +": " + str(value))

def is_tidy(number):
    num = str(number)
    for i in range(0, len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True

N = int(input())
for i in range(1,N+1):
    number = int(input())
    res = number
    while number > 1:
        if is_tidy(number):
            res = number
            break
        else:
            number -= 1

    pres(i, res)
