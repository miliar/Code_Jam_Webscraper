"""A
   Google CodeJam 2010
"""

from datetime import datetime

import os

def routine(Np, Mp):
    paths = Np
    paths.append('/')
    global added
    added = 0
    
    def addpath(p):
        head, tail = os.path.split(p)
        #print "split:", head, tail
        if head and tail and head not in paths:
            #print "recursing on:", head
            addpath(head)
            
        if p not in paths:
            #print "adding:", p
            paths.append(p)
            global added
            added += 1
        
    for m in Mp:
        #print "calling for:", m
        addpath(m)
    return added

if __name__ == '__main__':
    filename = "A-large"  #small-attempt0 large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        N, M = [int(x) for x in f.readline().split()]
        print N, M
        
        Np = []
        for i in xrange(N):
            Np.append(f.readline().strip())
        print Np
        Mp = []
        for i in xrange(M):
            Mp.append(f.readline().strip())
        print Mp

        print >>fo, "Case #%d: %s" % (case+1, routine(Np, Mp))

    fo.close()
    f.close()
    print datetime.now()
