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
            trace(args, ": got result from memo")
        except KeyError:
            result = f(*args)
            trace(args, ": got result by calling")
            memos[args] = result
        return result
    return memoized_f

# ------------------------------------------------------------------------------

n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    atrace( 'Case #', case_num )

    (C_farm_cost, F_production_rate, X_goal) = map(float, getline().split())
    trace(C_farm_cost, F_production_rate, X_goal)

    t_elapsed = 0.0
    min_t_so_far = None
    current_production_rate = 2.0

    while True:
        # Each time you buy a farm, your # of cookies drops to zero
        # because if you're going to buy a farm,
        # there's no point waiting till you have *more* cookies
        # than you need to buy it.

        # So our number of cookies here is zero.

        # Either we don't buy any more farms...
        t0 = t_elapsed + X_goal / current_production_rate
        trace('t0:', t0)

        if min_t_so_far is None or t0 < min_t_so_far:
            min_t_so_far = t0

        # ... or we buy at least one more farm as soon as we can:
        dt_to_buy_another_farm = C_farm_cost / current_production_rate

        t_elapsed += dt_to_buy_another_farm
        current_production_rate += F_production_rate

        if t_elapsed >= min_t_so_far:
            # It can't get any less, so give up
            break

    print 'Case #%d: %s' % (case_num, min_t_so_far)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
