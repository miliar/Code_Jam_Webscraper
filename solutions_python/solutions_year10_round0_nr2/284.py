#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    return
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

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

def GCD(values):
    for v in values: assert v > 0
    s = set(values)

    while True:
        if len(s) == 1:
            return s.pop()
        v_min = min(s)
        s_new = set()
        s_new.add(v_min)
        for v in s:
            rem = v % v_min
            if rem != 0:
                s_new.add(rem)
        s = s_new
        

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    data = map(int, getline().split())
    N = data[0]
    t_ = data[1:]
    assert len(t_) == N
    trace("times since events:", t_)
    ts_ = sorted(list(set(t_)))
    trace("uniquified & sorted:", ts_)
    tsm_ = [ t - ts_[0] for t in ts_[1:] ]
    trace("minus least:", tsm_)
    # Now, what is greatest common divisor of values in tsm_ ?
    T = GCD(tsm_)
    trace("largest possible integer factor T =", T)

    x = ts_[0] % T
    trace("most recent apocalypse occurred %d slarboseconds ago" % x)
    if x == 0:
        y = 0
    else:
        y = T - x
    trace("so next on/after now occurs in %d slarboseconds" % y)

    print 'Case #%d: %s' % (case_num, y)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
