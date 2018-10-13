#!/usr/bin/env python
""" template.py input-file > output-file"""

import sys
import numpy as np
from numpy import *

sys.setrecursionlimit(10000)

def input_words():
    line = IN.readline()
    return line.strip().split()

def input_ints():
    return map(int, input_words())

def input_floats():
    return map(float, input_words())

def format_sequence(s, formatter='%s'):
    return " ".join(map(lambda x: formatter % (x,), s))


def solve_one():
    """ XXX the real code comes here """
    D, N = input_words()
    D = float(D)
    N = int(N)

    K, S = [], []
    for i in range(N):
        Ki, Si = input_words()
        K.append(float(Ki))
        S.append(float(Si))

    K = np.array(K)
    S = np.array(S)

    arrivals = (D - K)/S
    our_speed = D / max(arrivals)
    
    return '%.6f' % (our_speed,)


if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    IN = open(sys.argv[1])

    T = input_ints()[0]
    
    for i in range(T):
        print "Case #%d:" % (i+1,), solve_one()
        sys.stderr.write("CASE #%d DONE\n" % (i+1,))
        sys.stderr.flush()


