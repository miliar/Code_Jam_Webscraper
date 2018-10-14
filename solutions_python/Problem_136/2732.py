#!/usr/bin/env python3

from sys import stdin
from decimal import *

if __name__ == '__main__':
    T = int(stdin.readline().strip())
    for i in range(1, T+1):
        C, F, X = map(Decimal, stdin.readline().strip().split(' '))
        R = 2
        time = Decimal(0)
        while ((X-C)/R) > (X/(R+F)):
            time += C/R
            R += F
        time += X/R
        print('case #{}: {:.7f}'.format(i, time))
