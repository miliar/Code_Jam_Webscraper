#!/usr/bin/python

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines();

# Quito primera linea que suele ser el numero de casos que hay
# y se puede deducir del numero de lineas del fichero restantes
lines = lines[1:]

n_case = 0
for line in lines:
    num = [int(c) for c in line.split(' ')]
    N, S, p = num[:3]
    num = num[3:]
    p *= 3
    ret = 0
    if p == 0:
        ret = len(num)
    elif p == 3:
        ret = len([e for e in num if e > 0])
    else:
        for score in num:
            if score >= (p - 2):
                ret += 1
            elif score >= (p - 4) and S:
                ret += 1
                S -= 1

    n_case += 1
    print("Case #"+str(n_case)+": "+str(ret))
