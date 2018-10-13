import sys

FILE = 'A-large.in'


import psyco
psyco.full()

def rs(f):
    return f.readline()[:-1]

def ri(f):
    return int(f.readline())

f = open(FILE, 'r')
sys.stdout = open(FILE + '.out', 'w')

ncases = int(f.readline())

for ncase in xrange(ncases):
    neng = ri(f)
    engs = [rs(f) for i in xrange(neng)]
    nqrs = ri(f)
    qrs = [rs(f) for i in xrange(nqrs)]
    
    sw = 0
    used = {}
    for qr in qrs:
        used[qr] = 1
        if len(used) == neng:
            sw += 1
            used = {}
            used[qr] = 1
    print 'Case #%d: %d' % (ncase+1, sw)
