#!/usr/bin/python

SIZE = 'small'
PROBLEM = 'C'
DATASET = PROBLEM + '-' + SIZE
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

SIZE = 25

table = [[0]*(SIZE+1) for i in xrange(SIZE+1)]
table[0][0] = 1

def prod(it):
    return reduce(lambda a,b:a*b, it, 1)

def comb(n, k):
    return prod(xrange(n-k+1,n+1))/prod(xrange(1,k+1))

def precompute():
    for col in xrange(1,SIZE+1):
        print col
        for lngth in xrange(1,col+1):
            source = col - lngth
            cnt = 0
            for prev_lngth in xrange(0,lngth+1):
                combs = comb(lngth-1, prev_lngth-1)
                cnt += combs * table[source][prev_lngth]
            table[col][lngth] = cnt

def solve(line):
    return results[int(line.strip())-1]

precompute()
results = [sum(a)%100003 for a in table]

raw_input()

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
T = int(ifile.readline())
for i in xrange(T):
    line = ifile.readline()
    ofile.write('Case #%s: %s\n' % (i+1,str(solve(line))))
ifile.close()
ofile.close()
