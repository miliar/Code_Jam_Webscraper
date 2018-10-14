#!/usr/bin/python

import sys

def main(infile):
    f = open(infile, "r")
    T = int(f.readline()[:-1])
    for i in range(0, T):
        C, F, X = map(float, f.readline()[:-1].split(" "))
        print "Case #" + str(i+1) + ": " + str(solve_case(C, F, X))
    f.close()

def solve_case(C, F, X):
    # print C, F, X
    sumTimeFarms = 0.
    cookieRate = 2.
    lastT = sys.float_info.max
    while 1:
        T = X / cookieRate + sumTimeFarms
        if T > lastT:
            return lastT
        sumTimeFarms += C / cookieRate
        cookieRate += F
        lastT = T
    return 0

if __name__ == "__main__":
    # solve_case(500., 4., 2000.)
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main("B-example.in")

