#!/usr/bin/env python

import numpy as np

#input_file = 'data'
input_file = 'A-small-attempt0.in'

f = open(input_file)
lines = f.read().splitlines()
f.close()

T = int(lines[0])
for i in xrange(T):
    ind = int(lines[10*i + 1])
    assert(ind in range(1, 5))
    l1 = [int(a) for a in lines[10*i + 1 + ind].split()]
#    print mat1

    ind = int(lines[10*i + 6])
    assert(ind in range(1, 5))
    l2 = [int(a) for a in lines[10*i + 6 + ind].split()]
#    print mat2

    l = list(set(l1).intersection(l2))
    # print l

    if not l:
        print "Case #%d: Volunteer cheated!" % (i+1)
    elif len(l) > 1:
        print "Case #%d: Bad magician!" % (i+1)
    else:
        print "Case #%d: %d" % (i+1, l[0])
