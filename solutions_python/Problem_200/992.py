from sys import *
from math import *

def tidy(digits):
    max_digit = 0
    max_index = 0
    too_high_index = -1
    for i in range(0, len(digits)):
        d = digits[i]
        if d > max_digit:
            max_digit = d
            max_index = i
        elif d < max_digit:
            too_high_index = max_index
            break

    if too_high_index == -1:
        return "".join([str(d) for d in digits])

    while too_high_index > 0 and digits[too_high_index-1] == max_digit:
        too_high_index -= 1

    digits[too_high_index] = max_digit - 1
    for i in range(too_high_index+1, len(digits)):
        digits[i] = 9

    result = "".join([str(d) for d in digits])
    if result[0] == '0':
        result = result[1:]
    return result

fin = open(argv[1] + ".in", 'r') 
fout = open(argv[1] + ".out", 'w')
    
ncases = int(fin.readline())
for c in range(0, ncases):
    digits = [ int(d) for d in fin.readline().split()[0] ]

    result = tidy(digits)
    fout.write("Case #" + str(c+1) + ": " + result + "\n")

fin.close()
fout.close()

