#!/usr/bin/env python
#
# URL: 
#

import math
import sys
import logging
import re
from collections import defaultdict
import tempfile

testdata = '''3
---+-++- 3
+++++ 4
-+-+- 4
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
    cakes,num = readmult(fhandle)
    num = int(num)
    logging.info('Test: %s %d', cakes, num)
    return solve(cakes, num)

def invert(x):
    if x == '-':
        return '+'
    return '-'

def solve(cakes, num):
    nflips = 0
    cakes = [x for x in cakes]
    for i in range(len(cakes)-num+1):
        if cakes[i] == '-':
            nflips += 1
            for j in range(i,i+num):
                cakes[j] = invert(cakes[j])
    if ''.join(cakes[-num:]) == '+' * num:
        return nflips
    else:
        return 'IMPOSSIBLE'

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
        ans = nextcase(ifhandle)
        outstr = 'Case #%d: %s' % (i+1, ans)
        logging.info(outstr)
        print >>ofhandle, outstr

    logging.info('Complete')
