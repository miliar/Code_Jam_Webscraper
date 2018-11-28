#!/usr/bin/env python
"""
RPI

Google Code Jam
2011 Round 1B
Problem A: RPI


Author: Kelsey Jordahl <kajord@gmail.com>
Time-stamp: <Sat May 21 13:34:46 EDT 2011>

"""

import sys
from numpy import *

verbose = True
debug = False

def rpi(m):
    '''
    Calculate RPI
    '''
    N = len(m)
    wp = zeros(N); owp = zeros(N); oowp = zeros(N)
    for i in xrange(N):
        wp[i] = nansum(m[:][i])/nansum(-isnan(m[:][i]))
    for i in xrange(N):
        opp = -isnan(m[:][i])
        M = nansum(opp)                    # number of opponents
        oppw = 0
        for j in xrange(N):
            if opp[j]:
                oo = m[:][j].copy()
                oo[i] = nan
                if debug:
                    print oo
                oppw += nansum(oo)/sum(-isnan(oo))
        owp[i] = oppw/M
        if verbose:
            print owp[i]
    # OOWP
    for i in xrange(N):
        opp = -isnan(m[:][i])
        M = nansum(opp)                    # number of opponents
        oppw = 0
        for j in xrange(N):
            if opp[j]:
                oppw += owp[j]
        oowp[i] = oppw/M
        if verbose:
            print 'wp: %6.5f, owp: %6.5f, oowp: %6.5f' % (wp[i],owp[i],oowp[i])
        
                
    return 0.25*wp + 0.5*owp + 0.25*oowp

def main():
    if len(sys.argv) < 2:
        infile = 'A-test.in'
    else:
        infile = sys.argv[1]
    if len(sys.argv) < 3:
        if infile[-3:] == '.in':
            outfile = infile[:-3] + '.out'
        else:
            outfile = infile + '.out'
    else:
        outfile = sys.argv[2]
    if verbose:
        print 'infile %s, outfile %s' % (infile, outfile)
    f = open(infile)
    o = open(outfile,'w')
    T = int(f.readline())
    print 'T = %d' % T
    for i in xrange(T):
        N = int(f.readline())
        for j in xrange(N):
            l = list(f.readline())
            a = zeros(N)
            if debug:
                print l
            for k in xrange(N):
                if l[k] == '.':
                    a[k] = 'nan'
                else:
                    a[k] = int(l[k])
            if j==0:
                m = a
            else:
                m = vstack((m,a))
        if verbose:
            print m
        r = rpi(m)
        print 'Case #%d:' % (i+1)
        o.write('Case #%d:\n' % (i+1))
        for res in r:
            print '%14.12f' % res
            o.write('%14.12f\n' % res)
    f.close
    o.close

if __name__ == '__main__':
    main()
