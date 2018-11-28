#!/usr/bin/env python
#
# URL: https://code.google.com/codejam/contest/4314486/dashboard
#

import math
import sys
import logging
import re
from collections import defaultdict
import tempfile

testdata = '''5
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1
26
26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
'''

alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
    num = readint(fhandle)
    nums = list(readmultint(fhandle))
    assert num == len(nums)
    logging.info('Test: %s', nums)
    return solve(nums)

def solve(nums):
    retlist = []
    N = len(nums)
    T = sum(nums)
    while max(nums) > 0:
        count = [i for i,x in enumerate(nums) if x > 0]
        logging.debug('nums %s, count %s', nums, count)
        if len(count) == 2:
            i,j = tuple(count)
            logging.debug('%d,%d * %d', i, j, nums[i])
            retlist = retlist + [alph[i]+alph[j]] * nums[i]
            nums[i] -= nums[i]
            nums[j] -= nums[j]
            assert sum(nums) == 0
            continue
        maxi = 0
        for i in range(N):
            if nums[i] > nums[maxi]:
                maxi = i
        retlist.append(alph[maxi])
        nums[maxi] -= 1
        logging.debug('list %s, ret %s', nums, retlist)
    logging.debug('assert %d %d', T, len([len(x) for x in retlist]))
    assert T == sum([len(x) for x in retlist])
    return retlist

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
        outstr = 'Case #%d: %s' % (i+1, ' '.join(ans))
        logging.info(outstr)
        print >>ofhandle, outstr

    logging.info('Complete')
