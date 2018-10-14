import linecache
import math

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

def is_square(num):
    sqroot = math.sqrt(num)
    if sqroot == int(sqroot):
        return int(sqroot)
    return False

cases = 100
lines = 100
filename = 'small.in'

case = 1
line = 1
while case <= cases and line <= lines:
    interval = linecache.getline(filename, line).split()
    start = int(interval[0])
    end = int(interval[1])
    
    fair_and_square = 0
    for num in range(start, end+1):
        if is_palindrome(num):
            #print('{}: Is palindrome'.format(num))
            sqroot = is_square(num)
            if sqroot:
                #print('{}: Is square root'.format(num))
                if is_palindrome(sqroot):
                    fair_and_square += 1
                    #print('{}: Square root is palindrome'.format(num))
 
    print('Case #{}: {}'.format(case, fair_and_square))
    case = case + 1
    line = line + 1





