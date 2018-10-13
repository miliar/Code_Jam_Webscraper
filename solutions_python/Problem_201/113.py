#!/usr/bin/env python

import math
import sys
import logging
import re
from collections import defaultdict
import tempfile

testdata = '''8
4 2
5 2
6 2
1000 1000
1000 1
500000 281623
194724 19432
924213 445262
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
    n,k = readmultint(fhandle)
    logging.info('Test: %d %d', n, k)
    return solve(n,k)

def solve(n,k):
    counts = defaultdict(lambda:0)
    counts[n] = 1
    while k > 0:
        m = max(counts)
        logging.debug('%d %s', k, counts)
        if counts[m] < k:
            counts[m/2] += counts[m]
            counts[(m-1)/2] += counts[m]
            k -= counts[m]
            del(counts[m])
        else:
            break
    m = max(counts)
    v = counts[m]
    return (m)/2, (m-1)/2

if __name__ == '__main__':
    
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
        ans1,ans2 = nextcase(ifhandle)
        outstr = 'Case #%d: %d %d' % (i+1, ans1, ans2)
        logging.info(outstr)
        print >>ofhandle, outstr

    logging.info('Complete')
