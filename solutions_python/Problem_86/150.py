import psyco
psyco.full()
import sys


def primesAsSet(pmax):
    cands = range(2,pmax)
    # set all non-primes in cands to 0
    # use multiples of numbers that don't get removed from cands
    n = 2
    while True:
        # reset any multiples that can be found
        for m in xrange(2*n,pmax,n):
            if m >= pmax:
                break
            cands[m-2] = 0
        
        # find next number to sweep with
        found = False
        for ci in xrange(n-2,pmax-2):
            c = cands[ci]
            if c > n:
                n = c
                found = True
                break
        if not found:
            break
    pss = set() # prime --> count (here always 1)
    for n in cands:
        if n != 0:
            pss.add(n)
    return pss


primes = sorted(list(primesAsSet(10000)))


def calc(notes,l,h):
    global primes
    if l <= 1:
        return 1
    
    for p in xrange(l,h+1):
        if p>h:
            break
        elif p>=l:
            found = True
            for n in notes:
                if n%p != 0 and p%n != 0:
                    found = False
                    break
            if found:
                return p
    return "NO"

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    n,l,h = [int(a) for a in line.split(' ')]
    notes = [int(a) for a in ig.next().split(' ')]
    
    v = calc(notes,l,h)
    print "Case #%d: %s" % (cn,v)
    cn += 1
