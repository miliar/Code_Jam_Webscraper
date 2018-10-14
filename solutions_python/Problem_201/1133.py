#!/usr/bin/env python3
import math
import sys

class MyOutput:

    def __init__(self):
        self.__count = 1

    def out(self, s):
        print("Case #{}: {}".format(self.__count, s))
        self.__count += 1
        

def parse_line(l):
    N, K = l.split()
    return int(N), int(K)

def solve(N, K):
    lP = math.ceil( math.log( K+1, 2 ) ) # float
    lPm = lP-1
    P = 2**lP
    Pm = 2**lPm
    rK = (K-Pm) / P
    hi = N / P - rK
    lo = (N - (P/2)) / P - rK
    return "{} {}".format(int(hi), int(lo))

def process(fd):
    count = int(fd.readline())
    myout = MyOutput()
    for i in range(count):
        res = solve( *parse_line( fd.readline() ) )
        myout.out(str(res))

def main(fname):
    with open(fname) as fd:
        data = process(fd)

def test():
    main("test.in")

#test()
main(sys.argv[1])
