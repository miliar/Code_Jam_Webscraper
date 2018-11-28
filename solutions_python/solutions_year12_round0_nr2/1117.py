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

max_best_sur_ = {}
max_best_unsur_ = {}
for total in range(0,1+30):
    max_best_sur_[total] = -1
    max_best_unsur_[total] = -1

for a in range(0, 1+10):
    max_possible_score = min(a+2,10)
    for b in range(a, 1+max_possible_score):
        for c in range(b, 1+max_possible_score):
            is_surprising = (c == a+2)
            total = a + b + c
            best = c
            trace(a, b, c, is_surprising, total, best)
            if is_surprising:
                max_best_sur_[total] = max(
                    max_best_sur_[total],
                    best)
            else:
                max_best_unsur_[total] = max(
                    max_best_unsur_[total],
                    best)

if 1:
    trace()
    for total in range(0, 1+30):
        trace(
            total,
            max_best_sur_[total],
            max_best_unsur_[total]
        )
        
n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    data = map(int,getline().split())
    N = data[0]
    S = data[1]
    p = data[2]
    t_ = data[3:]
    assert len(t_) == N
    
    trace('N=', N, 'S=', S, 'p=', p, 't=', t_)

    result_count = 0
    ns = 0
    for total in sorted(t_):
        mbs = max_best_sur_[total]
        mbu = max_best_unsur_[total]
        trace(total, mbs, mbu)
        if mbs == -1:
            # this can't be surprising
            mb = mbu
        else:
            # it could be surprising
            if ns < S:
                # haven't used up surprisings yet
                if mbs >= p and mbu < p:
                    # counting this as surprising makes a difference
                    # use the surprising
                    mb = mbs
                    ns += 1
                else:
                    mb = mbu
            else:
                # used up surprisings
                mb = mbu
        if mb >= p:
            result_count += 1

    print 'Case #%d: %s' % (case_num, result_count)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
