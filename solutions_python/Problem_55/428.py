#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys

ngrps = 0
grps = []
cap = 0
gmap = {}

# returns (nper, nextg)
def getNumPers( sg ):
    global gmap
    global grps
    global cap
    global ngrps

    if sg in gmap:
        return gmap[sg]
    
    nper = 0
    for n in xrange( sg, ngrps ):
        temp = nper + grps[n]
        if temp > cap:
            gmap[sg] = (nper, n)
            return (nper,n)
        nper = temp

    for n in xrange( 0, sg ):
        temp = nper + grps[n]
        if temp > cap:
            gmap[sg] = (nper, n)
            return (nper,n)
        nper = temp

    return (nper, sg) 

def main(argv):
    global gmap
    global grps
    global cap
    global ngrps

    f = open(argv[0], "rb")
    num = int(f.readline())
    
    for n in xrange(1,num+1):
        l = f.readline().split()
        runs = int( l[0] )
        cap = int( l[1] )
        ngrps = int( l[2] )
        grps = [ int(i) for i in f.readline().split() ]
        if len(grps) != ngrps:
            print "Error"
            return

        gmap = {}
        startg = 0
        money = 0
        for r in xrange(runs):
            m, ng = getNumPers( startg )
            money = money + m
            startg = ng
        
        print "Case #%d: %d" % (n, money)

if __name__ == "__main__":
    main(sys.argv[1:])

