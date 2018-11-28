#!/usr/bin/python
import sys

T = int(sys.stdin.readline())

for case in xrange(T):
    x = int(sys.stdin.readline())
    for i in xrange(x):
        A = set(map(int,sys.stdin.readline().split()))

    for i in xrange(4-x):
        sys.stdin.readline()

    x = int(sys.stdin.readline())
    
    for i in xrange(x):
        B = set(map(int,sys.stdin.readline().split()))
    z = A.intersection(B)
    
    if len(z) == 1:
        print "Case #%d: %d" % (case+1, (list(z)[0]))
    elif len(z) == 0:
        print "Case #%d: Volunteer cheated!" % (case+1)
    else:
        print "Case #%d: Bad magician!" % (case+1)
            
    for i in xrange(4-x):
        sys.stdin.readline()
