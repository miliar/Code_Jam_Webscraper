#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1,T+1):
        doCase(case)

def doCase(case):
    C, F, X = [float(n) for n in sys.stdin.readline().split()]
    oldY = float("inf")
    y = X / 2
    buyF = 1
    while y < oldY:
        oldY = y
        y =  X / (2 + buyF*F)
        for i in range(0,buyF):
            y += C / (2 + i*F)
        buyF +=1
    sys.stdout.write("Case #{}: {}\n".format(case, oldY))

if __name__ == '__main__':
    main()
