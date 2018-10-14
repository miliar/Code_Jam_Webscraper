import re, itertools, math

input = open('C:\\Users\\Adam\\Downloads\\A-small-attempt0 (1).in', 'r')
#input = open('C:\\Python27\\CodeJam\\1A 2013\\inputs.txt', 'r')
output = open('C:\\Python27\\CodeJam\\1A 2013\\outputs.out', 'w')

def solve(x, case):
    r = long(x[0])
    t = long(x[1])
    res = 0

    area = (r+1)**2 - r**2
    t = t - area
    
    while t >= 0:
        res = res + 1
        r = r + 2
        area = (r+1)**2 - r**2
        t = t - area
    result = "Case #" + str(case) + ": " + str(res)
    return result

case = 1
cases = int(input.readline())

while case <= cases:
    x = input.readline().split()
    print x
    result = solve(x, case)
    if case != cases:
        result = result + "\n"
    output.write(result)
    case += 1

output.close()
input.close()
            
