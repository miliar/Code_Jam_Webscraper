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
def mtrace(*strs):
    return
    atrace(*strs)

def atrace(*strs):
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
            mtrace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            mtrace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

# ------------------------------------------------------------------------------

n_cases = int(getline())
mtrace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    mtrace()
    atrace( 'Case #', case_num )

    [D] = map(int, getline().split())
    P_ = map(int, getline().split())
    assert len(P_) == D

    mtrace('D =', D)
    mtrace('P_ =', P_)

    maxp = max(P_)
    mtrace('maxp =', maxp)

    minutes_ = []
    for m in range(1, maxp+1):
        mtrace('  m =', m)
        c = sum( (p-1)/m for p in P_ )
        mtrace('    To make all stacks no higher than %d would require %d cuts' % (m, c))
        mtrace('    so that would take %d special minutes, followed by %d normal minutes' % (c, m))
        minutes_for_m = c + m
        mtrace('    total =', minutes_for_m)
        minutes_.append(minutes_for_m)

    min_minutes = min(minutes_)

    print 'Case #%d: %s' % (case_num, min_minutes)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
