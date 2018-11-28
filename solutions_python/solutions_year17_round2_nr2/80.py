#!/opt/local/bin/python

"""Premature optimization is the root of all evil."""

import sys
import re

def doiteasy(N, R, Y, B):
    if (R) > N // 2 or (B) > N // 2 or (Y) > N // 2:
        return "IMPOSSIBLE"
    elif R == 0 and B == 0 and Y == 0:
        return "?"
    dct = { 'R' : R, 'B': B, 'Y': Y }
    lst = sorted([list(d) for d in dct.items()], key = lambda x : -x[1])
    n = lst[1][1]
    out = (lst[0][0] + lst[1][0]) * n + "x"
    
    lst[0][1] -= n
    lst[1][1] = 0

    idx = 1
    while lst[2][1] > lst[0][1]:
        out = out[:idx] + lst[2][0] + out[idx:]
        idx += 2
        lst[2][1] -= 1

    out = out.replace('x', '')
    
    out = out + (lst[0][0] + lst[2][0]) * lst[2][1]
    
    return out


def doit(N, R, O, Y, G, B, V):
    if (O+V+R) > N // 2 or (G+V+B) > N // 2 or (O+G+Y) > N // 2:
        return "IMPOSSIBLE"
    if V > Y or O > B or G > R:
        return "IMPOSSIBLE"

    out = doiteasy(N, R-G, Y-V, B-O)
    if out == "IMPOSSIBLE":
        return out
    elif out == "?":
        if len([x for x in (R, B, Y) if x > 0]) != 1:
            return "IMPOSSIBLE"
        if R > 0:
            return 'RG' * G
        if B > 0:
            return 'BO' * O
        if Y > 0:
            return 'YV' * Y

    for a,b,c in [('R', 'RG', G), ('Y', 'YV', V), ('B', 'BO', O)]:
        try :
            x = out.index(a)
            out = out[:x] + b * c + out[x:]
        except ValueError:
            pass

    return out


T = int(sys.stdin.readline())
for casenum in range(T):
    data = [int(x) for x in sys.stdin.readline().split()]

    n = str(doit(*data))




    print("Case #" + str(casenum + 1) + ": " + n)
