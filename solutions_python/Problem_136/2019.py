#!/usr/bin/python
import decimal
import sys

D = decimal.Decimal
decimal.getcontext().prec = 14

def calc_time(C, F, X):
    rate = D(2.0)
    time = D(0.0)
    while True:
        if X / rate < X/(rate + F) + (C / rate):
            return time + X / rate
        else:
            time += C / rate
            rate += F


with open(str(sys.argv[1]), 'r') as f:
    f.readline()
    lines = f.readlines()
    for i,line in enumerate(lines):
        print 'Case #{:}: {:}'.format(i+1, calc_time(*map(D, line.split())))








