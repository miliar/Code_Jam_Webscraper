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

def nsplit(x):
    nondecr, rest = x[0], x[1:]
    while len(rest) > 0:
        if nondecr[-1] <= rest[0]:
            nondecr, rest = nondecr + rest[0], rest[1:]
        else:
            return nondecr, rest
    return nondecr, rest


def completed(x):
    nondecr, rest = nsplit(x)
    if rest == '':
        return nondecr
    
    if nondecr == '1':
        result = ''
    else:
        result = completed(str(int(nondecr) - 1))
        
    result += '9' * len(rest)
    return result


def solve_one():
    """ XXX the real code comes here """
    return completed(input_words()[0])


if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    IN = open(sys.argv[1])

    T = input_ints()[0]
    
    for i in range(T):
        print "Case #%d:" % (i+1,), solve_one()
        sys.stderr.write("CASE #%d DONE\n" % (i+1,))
        sys.stderr.flush()


