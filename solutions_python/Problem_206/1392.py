#!/usr/bin/python3

import sys
from decimal import *

def solve(D, horses):
    retval = False
    for Ki in horses.keys():
        Si = horses[Ki]
        speed = (Decimal(Si) * Decimal(D)) / (Decimal(D) - Decimal(Ki))
        if not retval:
            retval = speed
        elif speed < retval:
            retval = speed
    return retval

def main(f):
    lines = f.readlines()
    T = int(lines[0])

    index = 1
    for t in range(1,T+1):
        D, N = map(int, lines[index].split(" "))

        horses = {}
        for i in range(1, N+1):
            K, S = map(int, lines[index+i].split(" "))
            horses[K] = S
            
        print("Case #%s: %06f" % (t, solve(D, horses)))
        index = index + N + 1

if __name__ == "__main__":
    main(sys.stdin)
