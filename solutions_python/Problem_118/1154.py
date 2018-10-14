from math import *

filename = "C-small-attempt0"

def is_fair(num):
    return str(num)[::-1] == str(num)

def solve(a, b):
    count = 0

    for i in range(ceil(sqrt(a)), floor(sqrt(b)) + 1):
        if (is_fair(i)):
            square = i * i
            if (is_fair(square)):
                count += 1

    return count

fi = open(filename + ".in", "r")
fo = open(filename + ".out", "w")

cases = int(fi.readline())

for case in range(cases):
    line = fi.readline().replace("\n", "")
    a, b = [int(num) for num in line.split(" ")]
    result = solve(a, b)
    output = "Case #%d: %s" % (case + 1, result)
    print(output)
    fo.write(output + "\n")

fi.close()
fo.close()