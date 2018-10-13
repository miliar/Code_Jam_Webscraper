#!/usr/bin/env python
"""
Pseudominion

Google Code Jam
2011 Qual Round
Problem A: Speaking in Tongues


Author: Kelsey Jordahl <kajord@gmail.com>
Time-stamp: <Sat Apr 14 11:42:30 EDT 2012>

"""

import sys
from numpy import *

verbose = False
debug = False

def build_dict():
    input = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
    output = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""
    d = {}
    for i, c in enumerate(input):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            d[c] = output[i]
        else:
            d[c] = c
    d['q'] = 'z'                        # could be themselves?
    d['z'] = 'q'
    return d


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
    d = build_dict()
    f = open(infile)
    o = open(outfile,'w')
    T = int(f.readline())
    print 'T = %d' % T
    for i in range(0, T):
        line = f.readline().strip()
        outline = ''.join([d[c] for c in line])
        print outline
        o.write('Case #%d: %s\n' % (i+1, outline))
    f.close
    o.close

if __name__ == '__main__':
    main()
