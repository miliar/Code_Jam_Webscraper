import sys

def nine(number, p):
    for i in range(p, len(number)):
        number[i] = '9'
    return number

def fix(number, p):
    if p + 1 == len(number):
        return number
    if number[p] > number[p+1]:
        number[p] = str(int(number[p]) - 1)
        number = nine(number, p+1)
    return number

def ordnung(number):
    for i in reversed(range(len(number))):
        number = fix(number, i)
    return number

file_name = sys.argv[1]
with open(file_name) as file:
    T = int(file.readline())
    for x in range(T):
        number_list = list(str(int(file.readline())))
        number_list = ordnung(number_list)
        print('Case #{}: {}'.format(x+1, int(''.join(number_list))))


