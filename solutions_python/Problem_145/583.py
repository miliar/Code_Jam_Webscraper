#!/usr/bin/python3

import sys
import math
import fractions
#import collections

if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for case in range(T):

        [P, Q] = [int(X) for X in sys.stdin.readline().split("/")]
        tmp = fractions.Fraction(P, Q)
        P = tmp.numerator
        Q = tmp.denominator

        if P%2 == 1 and math.log(Q, 2)%1 == 0: # possible
            print("Case #", case+1, ": ", int(math.ceil(math.log(Q/P, 2))), sep="")
        else:
            print("Case #", case+1, ": ", "impossible", sep="")

