#!/usr/bin/env python3

import math
from decimal import Decimal

def number_of_farms(cost, win, delta_rate, init_rate=2):
    rval = math.ceil(win/cost - init_rate/delta_rate -1)
    if rval>=0:
        return rval
    else:
        return 0

def time_required(cost, win, delta_rate, init_rate=2):
    farms=number_of_farms(cost, win, delta_rate, init_rate)
    total_time=0
    for i in range(farms):
        total_time+=cost/init_rate
        init_rate+=delta_rate
    total_time+=win/init_rate
    return Decimal(total_time).quantize(Decimal('1.0000000'))

def file_parser(filename):
    fo=open(filename)
    cases=[]
    next(fo)
    for line in fo:
        cases.append([float(i) for i in line.strip().split()])
    return cases

def main(filename):
    cases=file_parser(filename)
    for num,case in enumerate(cases):
        out=time_required(case[0],case[2],case[1],2.0)
        print("Case #{0}: {1}".format(num+1,out))

if __name__=="__main__":
    from sys import argv
    main(argv[-1])
