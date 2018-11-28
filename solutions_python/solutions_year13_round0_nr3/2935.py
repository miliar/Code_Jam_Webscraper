#!/usr/bin/env python3

from math import sqrt, fabs
from util import read_p, write_p

epsilon = 0.0000001
def adjust(f):
    floor = int(f)
    if fabs(f - int(f)) < epsilon:
        return floor
    else:
        return f

def palindrome(n):
    if int(n) != n:
        return False

    s = str(n); l = len(s)
    for i in range(int(l/2)):
        if s[i] != s[l-i-1]:
            return False
    return True

def fsq(n, root):
    return palindrome(root) and palindrome(n)

first, *rest = read_p()
for idx, line in enumerate(rest):
    count = 0
    x, y = [int(n) for n in line.split()]
    for n in range(x, y+1):
        root = adjust(sqrt(n))
        if fsq(n, root):
            #print("{} --> {}".format(n, root))
            count += 1
    print("Case #{}: {}".format(idx+1, count))
