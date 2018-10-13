#!/usr/bin/python

import sys

with open(sys.argv[1], 'r') as f:
    T = int(f.readline().strip())

    for _t in xrange(1, T+1):
        g1 = int(f.readline().strip())
        A1 = []
        for i in xrange(4):
            A1.append(map(int, f.readline().strip().split()))

        g2 = int(f.readline().strip())
        A2 = []
        for i in xrange(4):
            A2.append(map(int, f.readline().strip().split()))

        intersects = set(A1[g1-1]).intersection(set(A2[g2-1]))
        
        if len(intersects) == 1:
            print 'Case #%d: ' % _t + '%d' % list(intersects)[0]
        elif len(intersects) == 0:
            print 'Case #%d: ' % _t + 'Volunteer cheated!' 
        else:
            print 'Case #%d: ' % _t + 'Bad magician!'
