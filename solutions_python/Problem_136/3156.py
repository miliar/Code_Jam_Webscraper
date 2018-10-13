#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys


def solve(C, F, X):
    lut = []
    farms = 0
    
    while True:
        cps = F * farms + 2.0
        cpds = cps / 10.0
        tx = X / cpds
        tf = C / cpds
        if farms == 0:
            tb = 0
        else:
            tb = lut[farms - 1]['tb'] + lut[farms - 1]['tf']
        tbptx = tb + tx
        lut.append({
            'farms': farms,
            'cps': cps,
            'cpds': cpds,
            'tx': tx,
            'tf': tf,
            'tb': tb,
            'tbptx': tbptx
        })
        
        if farms > 0 and lut[-2]['tbptx'] < lut[-1]['tbptx']:
            return lut[-2]['tbptx'] / 10.0
        
        farms += 1


def main():
    cases = int(sys.stdin.readline().strip())
    for case in xrange(cases):
        C, F, X = map(float, sys.stdin.readline().strip().split(' '))
        print 'Case #%d: %.7f' % (case + 1, solve(C, F, X))
    return 0


if __name__ == '__main__':
    sys.exit(main())

