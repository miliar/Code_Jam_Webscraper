#!/usr/bin/env python
""" template.py input-file > output-file"""

import sys
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


from collections import defaultdict


def solve(N, K):
    d = defaultdict(lambda : 0)
    d[N] = 1
    for i in xrange(K):
        target = max(d.keys())
        splits = (target)//2, (target-1)//2
        d[target] -= 1
        if d[target] == 0:
            del d[target]
        d[splits[0]] += 1
        d[splits[1]] += 1
        #print 'step', i, 'target', target, splits, dict(d)
    return splits


def solve_one():
    """ XXX the real code comes here """
    N, K = input_words()
    N, K = int(N), int(K)
    tmp = solve(N, K)
    return str(tmp[0]) + ' ' + str(tmp[1])
    

if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    IN = open(sys.argv[1])

    T = input_ints()[0]
    
    for i in range(T):
        print "Case #%d:" % (i+1,), solve_one()
        sys.stderr.write("CASE #%d DONE\n" % (i+1,))
        sys.stderr.flush()


