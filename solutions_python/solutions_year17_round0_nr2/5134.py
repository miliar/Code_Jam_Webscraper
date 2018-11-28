#!/bin/python3

def is_tidy(number):
    pre = -1
    for i in number:
        if int(i) >= pre:
            pre = int(i)
        else:
            return False
    return True

f = open('input','r')
output = open('output', 'w')

N = f.readline()
result = ''

for i in range(1,int(N)+1):
    number = int(f.readline())

    while not is_tidy(str(number)):
        number -= 1

    result += 'Case #{}: {}\n'.format(i, number)

output.write(result)