#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

class Bunch:
    def __init__( self, **kwds ):
        self.__dict__ = kwds

pause_after_trace = False
def trace(*strs):
    return
    f = sys.stderr
    print >> f, '..',
    for str in strs:
        print >> f, str,
    print >> f
    if pause_after_trace:
        response = raw_input('? ')
        if response == 'q':
            sys.exit(1)

def memoize(f):
    memos = {}
    def memoized_f( *args ):
        try:
            result = memos[args]
            trace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            trace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    (A,B) = map(int, getline().split())

    foo = {}
    for num in range(A,B+1):
        s = str(num)
        rots = []
        for i in range(len(s)):
            r = s[i:] + s[:i]
            rots.append(r)
        minrot = sorted(rots)[0]
        trace(num, 'has rots:', rots, 'minrot=', minrot)

        foo.setdefault(minrot, []).append(num)

    tot_n_pairs = 0
    for (minrot, ilist) in foo.items():
        k = len(ilist)
        n_pairs = k * (k-1) / 2
        trace( minrot, ilist, k, n_pairs )
        tot_n_pairs += n_pairs

    print 'Case #%d: %s' % (case_num, tot_n_pairs)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
