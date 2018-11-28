__author__ = 'shiva'
import math

import sys

text = sys.stdin.readlines()

def howmanyfriends(l):
    b = 0
    s = 0
    for a in range(len(l)):
        c = int(l[a])
        if a == 0 and c > 0:
            s += c
        elif a == 0:
            continue
        else:
            if a <= s:
                s += c
            else:
                if c > 0:
                    b += int(math.fabs(s - a))
                    l[0] = str(int(l[0]) + b)
                    s += b + 1


    return b


for n in range(1, len(text)):
    lst = text[n][2:]
    lst = list(lst)
    print("Case #" + str(n) + ": " + str(howmanyfriends(lst[:-1])))











