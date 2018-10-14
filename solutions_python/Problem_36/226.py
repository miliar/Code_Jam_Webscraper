#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr


def solve( haystack, needle ):

    def f( x, y ):
    # Looking at the first x characters of the haystack,
    # how many ways are there to find a subsequence
    # consisting of the first y characters of the needle?
    # (how many sequences-of-indexes-of-length-y)
        if y == 0:
            k = 1
        elif x == 0:
            k = 0
        elif haystack[x-1] == needle[y-1]:
            k = wf( x-1, y ) + wf( x-1, y-1 )
        else:
            k = wf( x-1, y )
        return k % 10000

    a = {}
    def wf( x, y ):
        try:
            return a[(x,y)]
        except KeyError:
            r = f(x,y)
            a[(x,y)] = r
            return r

    return wf( len(haystack), len(needle) )

# -----

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    greeting = 'welcome to code jam'
    answer = solve( getline(), greeting )

    print 'Case #%d: %04d' % (case_num, answer)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
