"""C
   Google CodeJam 2010
"""

from datetime import datetime

def routine(R, k, N, g):
    t = 0   #total
    p = 0   #queue pointer
    for i in xrange(R):
        rt = 0  #ride total
        pc = 0  #people count
        while rt+g[p] <= k:
            if pc >= N:
                break  #all people are on board
            rt += g[p]
            p = (p+1) % N
            pc += 1
        t += rt
            
    return t

if __name__ == '__main__':
    filename = "C-small-attempt0"  #small
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        R, k, N = [int(x) for x in f.readline().split()]
        print R, k, N
        
        g = [int(x) for x in f.readline().split()]
        print g

        print >>fo, "Case #%d: %s" % (case+1, routine(R, k, N, g))

    fo.close()
    f.close()
    print datetime.now()
