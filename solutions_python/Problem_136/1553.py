#!python2
from __future__ import division, print_function

import sys
from pprint import pprint as pp
import math as m
from itertools import count

def result_no(C, F, X):
    print(str((C, F, X)), file=sys.stderr)
    i = int(m.ceil((F*X - 2*C - F*C) / F*C))
    print(i, file=sys.stderr)
    return (
        sum((C/(2+j*F)) for j in xrange(i+1))  # time to build i farms
        + (X / (2+i*F))  # time to finally get the wanted cookies
    )

def result(C, F, X):
    t = 0
    R = 2
    for i in count():
        time_no_other_farm = X/R
        time_next_farm = C/R
        time_no_other_farm_NEXT = X/(R+F)
        if time_no_other_farm < time_next_farm + time_no_other_farm_NEXT:
            t += time_no_other_farm
            break
        else:
            t += time_next_farm
            R += F
    return t

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        c, f, x = [float(s.strip()) for s in
                   sys.stdin.readline().strip().split()]
        print("Case #{}: {:.7f}".format(str(t+1), result(c, f, x)))
