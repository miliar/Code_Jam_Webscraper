import sys
import psyco
psyco.full()

FILE = 'A-large.in'
#FILE = 'input.txt'
f = open(FILE, 'r')
sys.stdout = open(FILE + '.out', 'w')

def rs():
    return f.readline()[:-1]

def ri():
    return int(f.readline())

def ra():
    return [int(s) for s in rs().split()]


ncases = int(f.readline())

for ncase in xrange(1, ncases+1):
    s = ri()
    v0 = ra()
    v1 = ra()
    
    v0.sort()
    v1.sort(reverse=True)
    t = sum(v0[i] * v1[i] for i in xrange(s))
        
    print 'Case #%d: %d' % (ncase, t)
