import sys
import psyco
psyco.full()

FILE = 'B-large.in'
f = open(FILE, 'r')
sys.stdout = open(FILE + '.out', 'w')

def rs():
    return f.readline()[:-1]

def ri():
    return int(f.readline())

def ph(s):
    s = s.split(':')
    return int(s[0]) * 60 + int(s[1])



ncases = int(f.readline())

for ncase in xrange(1, ncases+1):
    tat = ri()
    s = rs().split()
    na = int(s[0])
    nb = int(s[1])
    a = []
    b = []
    for i in xrange(na):
        s = rs().split()
        a.append((ph(s[0]), 'd'))
        b.append((ph(s[1]) + tat, 'a'))
    for i in xrange(nb):
        s = rs().split()
        b.append((ph(s[0]), 'd'))
        a.append((ph(s[1]) + tat, 'a'))
    a.sort()
    b.sort()
    av = 0
    lra = 0
    for h, t in a:
        if t == 'd':
            if av == 0:
                lra += 1
            else:
                av -= 1
        else:
            av += 1
    bv = 0
    lrb = 0
    for h, t in b:
        if t == 'd':
            if bv == 0:
                lrb += 1
            else:
                bv -= 1
        else:
            bv += 1
    print 'Case #%d: %d %d' % (ncase, lra, lrb)
