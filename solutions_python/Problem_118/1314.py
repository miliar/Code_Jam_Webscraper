#!/usr/bin/env python3
import math

def isFair(n):
    num = n
    rev = 0
    while num > 0:
        dig = num %  10
        rev = rev *  10 + dig
        num = num // 10
    return n == rev

fin  = open("C-small-attempt0.in",  "r")
fout = open("C-small.out", "w")

T = int(fin.readline())

for t in range(1, T + 1):
    A, B = [int(i) for i in fin.readline().split(" ")]
    lo = int(math.sqrt(A - 1)) + 1
    hi = int(math.sqrt(B)) + 1
    fairs = filter(isFair, range(lo, hi))
    squares = map(lambda x: x ** 2, fairs)
    n = len(list(filter(isFair, squares)))
    fout.write("Case #{0}: {1}\n".format(t, n))

fin.close()
fout.close()
