#!/usr/bin/python

# google code jam - c.durr - 2009
# Watersheds
# graph exploration


import sys, string


def sink(p):
    ''' returns the sink to which p will flood,
        and shortens the mapping on the way.
        ''' 
    if p in down:
        down[p] = sink(down[p])
        return down[p]
    else:
        return p

    
t = int(sys.stdin.readline())

for test in range(t):
    h,w = [int(i) for i in sys.stdin.readline().split()]
    
    # read elevations
    e = {}
    for i in range(h):
        l = [int(a) for a in sys.stdin.readline().split()]
        for j in range(w):
            e[(i,j)] = l[j]

    # construct direction of flow
    down = {}
    for p1 in e:
        for (di,dj) in [(-1,0),(0,-1),(0,+1),(+1,0)]:
            (i,j) = p1
            p2 = (i+di, j+dj)
            if p2 in e and e[p2]<e[p1] and \
                   (not p1 in down or e[p2]<e[down[p1]]): 
                    down[p1] = p2

    print 'Case #%d:' % (test+1)
    k = 0      # k is the number of sinks found so far
    name = {}  # name is the associated sink name
    for i in range(h):
        for j in range(w):
            p = sink((i,j))
            if not p in name:
                name[p] = string.ascii_lowercase[k]
                k+=1
            print name[p],
        print
