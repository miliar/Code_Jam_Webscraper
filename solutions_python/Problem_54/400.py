#!/usr/bin/python

DATASET = 'large'
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

def get_gcd(a,b):
    if a is None: return b
    def gcd_impl(a,b):
        while b != 0:
            a,b = b,a%b
        return a
    if a>=b: return gcd_impl(a,b)
    else: return gcd_impl(b,a)

def solve(events):
    diffs = [(lambda x: x if x>0 else -x)(events[i] - events[i+1]) for i in xrange(len(events)-1)]
    gcd = reduce(get_gcd, diffs)
    m = min(events)
    return (-m)%gcd

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
C = int(ifile.readline())
for i in xrange(C):
    print i,C
    line = ifile.readline().split(' ')
    N = int(line[0])
    assert(len(line) == N+1)
    events = [int(a) for a in line[1:]]
    ofile.write('Case #%s: %s\n' % (i+1, solve(events)))
ifile.close()
ofile.close()
