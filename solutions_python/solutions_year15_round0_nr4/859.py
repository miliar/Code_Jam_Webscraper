import math
from sys import stdin

file = open("output.txt", "w+")

def choose(n, bool):
    str = ""
    if (bool):
        str = "GABRIEL"
    else:
        str = "RICHARD"
    file.write("Case #%d: %s\n" %(n, str))

N = int (stdin.readline())

for t in range(N):
    x, r, c = stdin.readline().split()
    x, r, c = int(x), int(r), int(c)
    can = False
    if (((r * c) % x == 0) and x < 8):
        val = min(r, c)
        can = False
        if (x == 3 and val < 2):
            x
        elif ((x == 4 or x == 5) and val < 3):
            x
        elif (x in range(6, 7) and val < 4):
            x
        elif (x == 7 and val < 5):
            x
        else:
            can = True
    choose(t + 1, can)
