#!/usr/bin/env python
"""
Square tiles

Google Code Jam
2011 Round 1C
Problem A: Square Tiles

"""

import sys
from numpy import *

verbose = False
debug = False

def fix(m):
    '''
    replace blue with red
    '''
    R = len(m)
    C = len(m[0])
    if verbose:
        print 'R, C = %d, %d' % (R, C)
    r = []
    for i in xrange(R):
        r = r + ['']
        if debug:
            print m[i]
        if i==R-1:
            for j in xrange(C):
                if m[i][j] == '#':
                    return None
            r[i] = ''.join(m[i])
            return r
        for j in xrange(C-1):
            if i == R-1:
                return None             # last row
            if m[i][j] == '#':
                m[i][j] = '/'
                if m[i][j+1] != '#':
                    return None
                else:
                    m[i][j+1] = '\\'
                if m[i+1][j] != '#':
                    return None
                else:
                    m[i+1][j] = '\\'
                if m[i+1][j+1] != '#':
                    return None
                else:
                    m[i+1][j+1] = '/'
        if m[i][C-1] == '#':
            if verbose:
                print '# at EOL'
            return None
        r[i] = ''.join(m[i])

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
        l = f.readline().split()
        R = int(l[0])
        C = int(l[1])
        m = []
        for j in xrange(R):
            m = m + ['']
            m[j] = list(f.readline().rstrip())
        r = fix(m)
        print 'Case #%d:' % (i+1)
        o.write('Case #%d:\n' % (i+1))
        if r is None:
            print 'Impossible'
            o.write('Impossible\n')
        else:
            for j in xrange(R):
                print r[j]
                o.write('%s\n' % r[j])
    f.close
    o.close

if __name__ == '__main__':
    main()
