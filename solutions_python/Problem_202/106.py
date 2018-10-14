#!/usr/bin/env python

import math
import sys
import logging
import re
from collections import defaultdict
import tempfile

testdata = '''4
2 0
3 0
4 0
4 4
o 1 2
o 2 4
o 3 1
o 4 3
20 1
o 1 1
20 1
o 1 2
20 1
o 1 3
20 1
o 1 4
20 1
o 1 5
20 1
o 1 6
20 1
o 1 7
20 1
o 1 8
20 1
o 1 9
20 1
o 1 10
20 1
o 1 20
20 0
20 19
o 1 2
o 2 4
o 3 6
o 4 8
o 5 10
o 6 12
o 7 14
o 8 16
o 9 18
o 10 20
o 12 1
o 13 3
o 14 5
o 15 7
o 16 9
o 17 11
o 18 13
o 19 15
o 20 17
o 20 19
2 0
1 1
o 1 1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2
3 3
+ 1 1
+ 1 2
+ 1 3
3 3
+ 1 1
x 1 2
+ 1 3
3 3
+ 1 1
+ 1 2
x 1 3
10 1
+ 1 5
67 2
x 1 34
+ 1 19
100 6
+ 1 29
+ 1 4
+ 1 27
+ 1 7
+ 1 81
+ 1 33
100 3
+ 1 1
+ 1 2
+ 1 3
92 2
+ 1 69
o 1 14
'''

def readstr(fhandle):
    return fhandle.readline().strip()

def readone(fhandle):
    return int(fhandle.readline().strip())

def readint(fhandle):
    return readone(fhandle)

def readmult(fhandle):
    return tuple(fhandle.readline().strip().split())

def readmultint(fhandle):
    return tuple(int(x) for x in readmult(fhandle))

def readfirst(fhandle):
    ncases = readone(fhandle)
    return ncases

def nextcase(fhandle,params=None):
    n,m = readmultint(fhandle)
    marr = [readmult(fhandle) for i in range(m)]
    logging.info('Test: %d %s', n, marr)
    return solve(n,marr)

def islegal(r,c,t,h,n):
    countr = defaultdict(lambda:0,{t:1})
    countc = defaultdict(lambda:0,{t:1})
    countd1= defaultdict(lambda:0,{t:1})
    countd2= defaultdict(lambda:0,{t:1})
    #logging.debug('islegal? %d %d %s', r, c, t)
    for i in range(1,n+1):
        if i != c:
            countr[h[r,i]] += 1
        if i != r:
            countc[h[i,c]] += 1
            countd1[h[i,r+c-i]] += 1 # i+? == r+c
            countd2[h[i,-r+c+i]] += 1 # i-? == r-c
    #logging.debug('%s', dict(countr))
    if countr['x']+countr['o'] > 1: return False
    #logging.debug('%s', dict(countc))
    if countc['x']+countc['o'] > 1: return False
    #logging.debug('%s', dict(countd1))
    if countd1['+']+countd1['o'] > 1: return False
    #logging.debug('%s', dict(countd2))
    if countd2['+']+countd2['o'] > 1: return False
    logging.debug('True %s %s', dict(countd1), dict(countd2))
    #for r in range(1,n+1):
    #    logging.debug('%s', ''.join(h[r,c] for c in range(1,n+1)))
    return True

def solve(n,marr):
    h = defaultdict(lambda:'.')
    for (t,x,y) in marr:
        h[int(x),int(y)] = t
    logging.debug('Start hash %s', h)
    for r in range(1,n+1):
        logging.debug('%s', ''.join(h[r,c] for c in range(1,n+1)))
    '''
    Notes:
    per row: each pair must contain a +
    per col: each pair must contain a +
    per dia: each pair must contain a x
    * at most one non + per row
    * at most one non + per col
    * at most one non x per diag
    '''
    did_upgrade = True
    upgrades = []
    while did_upgrade:
        did_upgrade = False
        for r in [1,n]:
            for c in range(1,n+1):
                if h[r,c] == '.':
                    if islegal(r,c,'o',h,n):
                        h[r,c] = 'o'
                        did_upgrade = True
                        upgrades.append(('o',r,c))
                        #break
                    elif islegal(r,c,'+',h,n):
                        h[r,c] = '+'
                        did_upgrade = True
                        upgrades.append(('+',r,c))
                        #break
                if h[r,c] == 'x' or h[r,c] == '+':
                    if islegal(r,c,'o',h,n):
                        h[r,c] = 'o'
                        did_upgrade = True
                        upgrades.append(('o',r,c))
                        #break
        for r in range(1,n+1):
            for c in range(1,n+1):
                if h[r,c] == '.':
                    if islegal(r,c,'x',h,n):
                        h[r,c] = 'x'
                        did_upgrade = True
                        upgrades.append(('x',r,c))
                        #break
        if did_upgrade:
            logging.debug('upgrades: %s', upgrades)
    val = 0
    for r in range(1,n+1):
        logging.debug('%s', ''.join(h[r,c] for c in range(1,n+1)))
        for c in range(1,n+1):
            if h[r,c] == 'x' or h[r,c] == '+':
                val += 1
            elif h[r,c] == 'o':
                val += 2

    logging.debug('n=%d val=%d %s', n, val, upgrades)
    assert n < 2 or val == 3*n-2
    return val,upgrades

def exhaustn(h,n,i,j):
    if i > n or j > n:
        score = h.values().count('+')+h.values().count('x')+2*h.values().count('o')
        if n == 2 and score < 4: return
        if n == 3 and score < 7: return
        if n == 4 and score < 10: return
        if n == 5 and score < 13: return
        if n == 6 and score < 16: return
        print 'Score:', score
        for x in range(1,n+1):
            print ''.join(h[x,y] for y in range(1,n+1))
        print
        return
    for t in ['.','x','+','o']:
        #print i, j, t
        _h = h.copy()
        d = defaultdict(lambda:'.',_h)
        if islegal(i,j,t,d,n):
        #    print 'legal', i, j, h, t
            if j+1 > n:
                _i = i + 1
                _j = 1
            else:
                _i = i
                _j = j+1
            _h = h.copy()
            _h[i,j] = t
            exhaustn(_h,n,_i,_j)
        #else:
        #    print 'not legal', i, j, h, t

if __name__ == '__main__':

    #exhaustn({},1,1,1)
    #exhaustn({(1,1):'o',(1,2):'+',(1,3):'+',(1,4):'+',(1,5):'+'},5,2,1)
    #exhaustn({(1,1):'o',(1,2):'+'},5,1,3)
    #exhaustn({(1,1):'+',(1,2):'+',(1,3):'+',(1,4):'+',(1,5):'+',(1,6):'o'},6,2,1)
    #sys.exit(0)
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--test',help='test cases',action='store_true',default=False)
    parser.add_argument('-d','--debug',action='count',default=0)
    parser.add_argument('inputfile',nargs='?')
    args = parser.parse_args()

    if args.debug >= 1:
        logging.basicConfig(level=logging.DEBUG,stream=sys.stdout)
    else:
        logging.basicConfig(level=logging.CRITICAL,stream=sys.stderr)

    ifhandle = sys.stdin
    if args.inputfile:
        ifhandle = open(args.inputfile)
    if args.test:
        ifhandle = tempfile.TemporaryFile()
        ifhandle.write(testdata)
        ifhandle.seek(0)
    ofhandle = sys.stdout

    nparams, ncases = 0, readfirst(ifhandle)

    # parameter reading
    logging.debug('%d parameters', nparams)
    for i in range(nparams):
        pass

    # test case reading
    logging.debug('%d cases', ncases)
    for i in range(ncases):
        val,upgrades = nextcase(ifhandle)
        outstr = 'Case #%d: %d %d' % (i+1, val, len(upgrades))
        logging.info(outstr)
        print >>ofhandle, outstr
        for (t,r,c) in upgrades:
            outstr = '%s %d %d' % (t,r,c)
            logging.info(outstr)
            print >>ofhandle, outstr

    logging.info('Complete')

'''
Score: 2
o

Score: 4
o+
.x

Score: 7
o++
.x.
.+x

Score: 10
o+++
.x..
..x.
.++x

Score: 13
o++++
.x...
..x..
...x.
.+++x

Score: 16
o+++++
.x....
..x...
...x..
....x.
.++++x

Score: 16
+o++++
x.....
..x...
...x..
....x.
.++++x

Score: 16
++o+++
x.....
.x....
...x..
....x.
.++++x

Score: 16
+++++o
x.....
.x....
..x...
...x..
.+++o.




'''
