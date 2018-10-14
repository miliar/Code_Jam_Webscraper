import fileinput
import math

def solve(x, r, c):
    if (x == 1):
        return True
    if (x > 6):
        return False
    if (x > r and x > c):
        return False

    if (x % 2 == 0):
        size = (x / 2, x / 2 + 1)
    else:
        size = ((x + 1) / 2, (x + 1) / 2)

    if (x > 3):
        if ((size[0] >= r and size[1] >= r) or (size[0] >= c and size[1] >= c)):
            return False
    else:
        if ((size[0] > r and size[1] > r) or (size[0] > c and size[1] > c)):
            return False

    if (r * c % x == 0):
        return True
    return False

input = fileinput.input()

cases = int(input.readline())
for num in range(cases):
    case = input.readline().split()
    x = int(case[0])
    r = int(case[1])
    c = int(case[2])
    winner = "GABRIEL" if solve(x, r, c) else "RICHARD"
    print "Case #" + str(num + 1) + ": " + winner
