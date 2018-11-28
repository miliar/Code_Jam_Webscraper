#!/usr/bin/env python
# vim: set tabstop=4 shiftwidth=4 expandtab
from __future__ import with_statement

from contextlib import nested
from os.path import expanduser, join
import os
from pdb import set_trace
from time import clock
from shutil import copy

in_fn = 'in'
out_fn = 'out'

this_file = join(os.getcwd(), __file__)
desktop = join(expanduser('~'), 'Desktop')
copy(this_file, desktop)

def process(input):
    lines = input.splitlines()
    N = int(lines[0])

    samples = lines[1:N+1]
    print samples

    def permutations(L):
        if len(L) <= 1:
            yield L
        else:
            a = [L.pop(0)]
            for p in permutations(L):
                for i in range(len(p)+1):
                    yield p[:i] + a + p[i:]
    
    def compute_test_case(sample):
        L = [int(i) for i in sample] + [0]
        print L

        perms = {}

        for p in permutations(L):
            print p
            p_str = ''.join( map(str, p) )
            if int(p_str) not in perms:
                # and not p_str.startswith('0'):
                perms[int(p_str)] = True

        K = perms.keys()
        K.sort()
        # print K 
        # print sample
        I = K.index( int(sample) )
        # print I
        return K[I+1]

    start = clock()
    cnt = compute_test_case('12345') # samples[1])
    print "Time taken (seconds) = %.6f" % (clock()-start)
    # return cnt
    
    out = []
    for i, sample in enumerate(samples): 
        print i
        case = 'Case #%d: %s' % (i+1, compute_test_case(sample))
        out.append(case)

    res =  os.linesep.join(out) + os.linesep
    print res
    return res

    # test
    if True:
        with open(out_fn) as f:
            return f.read()

if __name__ == "__main__":

    if True:
        with open(in_fn) as f:
            input = f.read()
            output = process(input)

            out_fn = join(expanduser('~'), 'Desktop', 'out.txt')
            with open(out_fn, 'w') as fo:
                fo.write(output)

    import sys
    sys.exit(0)
    
    test = True
    if test:
        with nested(open(in_fn), open(out_fn)) as (f_in, f_out):
        
            input = f_in.read()
            output = f_out.read()
            assert process(input) == output
            print 'Youpi'
