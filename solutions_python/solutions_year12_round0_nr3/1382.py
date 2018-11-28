import psyco
psyco.full()
import sys, math, time, itertools

rotsMap = {} # num : (rot, rot, ...)

def updateRotsMap(n):
    nMin,nMax = 1,2000000
    if not rotsMap.has_key(n):
        rn = str(n)
        rots = [rn[-c:] + rn[0:-c] for c in xrange(len(rn))]
        rotInts = list(sorted(set([int(r) for r in rots if r[0]!='0'])))
        rotIntsClipped = [r for r in rotInts if (r>=nMin and r<=nMax)]
        for ir in rotIntsClipped:
            rotsMap[ir] = rotIntsClipped

#for n,rots in rotsMap.items():
#    print n, rots
#raise

def bincoeff(n,k):
    fact = math.factorial
    return fact(n) / (fact(k) * fact(n-k))

def calc(A,B):
    y = 0
    incs = set()
    for n in xrange(A,B+1):
        updateRotsMap(n)
        if not n in incs:
            rots = [r for r in rotsMap[n] if (r>=A and r<=B)]
            incs.update(rots)
            if len(rots) > 1:
                y += bincoeff(len(rots), 2)
            #print "sdsdf", A,B,n,rots
        else:
            pass
            #print "sdfsdf", A,B,n,[]
    return y
            


#print len(rotsMap), max(rotsMap.keys())

def timed(func):
    startTime = time.time()
    r = func()
    print "result: %s, took %.0f secs" % (str(r), time.time()-startTime)

#timed(lambda: calc(10000,2000000))
#timed(lambda: calc(1,2000000))
#timed(lambda: calc(1,2000000))



def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    A,B = [int(s) for s in line.split(" ")]
    v = calc(A,B)
    print "Case #%d: %s" % (cn,v)
    cn += 1


#print "DEBUG"
#for n,rots in rotsMap.items():
#    print n,rots
