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


flip = lambda s: ''.join([chr(ord('+')+ord('-')-ord(x)) for x in s])

def flips_needed(s, K):
    count = 0
    for i in xrange(len(s) - K + 1):
        if s[i] == '-':
            s = s[:i] + flip(s[i:i+K]) + s[i+K:]
            count += 1
    if '-' in s:
        return 'IMPOSSIBLE'
    else:
        return str(count)

    
def solve_one():
    """ XXX the real code comes here """
    s, K = input_words()
    K = int(K)
    return flips_needed(s, K)
    

if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    IN = open(sys.argv[1])

    T = input_ints()[0]
    
    for i in range(T):
        print "Case #%d:" % (i+1,), solve_one()
        sys.stderr.write("CASE #%d DONE\n" % (i+1,))
        sys.stderr.flush()


