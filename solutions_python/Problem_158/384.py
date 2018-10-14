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

    (X,R,C) = map(int, getline().split())
    mtrace('X =', X)
    mtrace('R,C =', R, C)

    Richard = 'RICHARD'
    Gabriel = 'GABRIEL'

    if X == 1:
        # There is only 1 1-omino,
        # so Richard has no choice.
        # And regardless of RxC,
        # Gabriel can fill it with 1-ominoes.
        winner = Gabriel
    elif X == 2:
        # There is only 1 2-omino,
        # so Richard has no choice.
        # But depending on R and C,
        # Gabriel may not be able to fill the grid.
        if R % 2 == 0 or C % 2 == 0:
            # Gabriel can always fill the grid.
            winner = Gabriel
        else:
            # Gabriel can't fill the grid.
            winner = Richard

    elif X in [3,4,5,6]:
        # Can Richard pick an X-omino
        # that can't itself fit into the given grid?
        # If so, he wins.
        if max(R,C) < X:
            # Richard can pick the 1-by-X omino
            winner = Richard
        elif min(R,C) <= (X-1)/2:
            # Richard can pick an L-shape
            # whose smaller dimension exceeds the smaller dimension of the grid,
            winner = Richard
        else:
            # Whichever piece Richard picks, it will at least fit in the grid.
            # So Gabriel may have a chance.
            if (R * C) % X != 0:
                # But the grid can't possibly be partitioned into X-ominoes,
                # so Gabriel doesn't have a chance.
                winner = Richard
            else:
                # And the grid can be partitioned into X-ominos,
                # so Gabriel may still have a chance.
                # But it's possible that Richard can pick a piece that,
                # regardless of how Gabriel places it,
                # divides the grid into 2 or more regions
                # that *can't* be partitioned into X-ominoes.

                if X == 4 and (R,C) in [(2,4), (4,2)]:
                    # Richard can pick a T shape or a W shape.
                    winner = Richard
                elif X == 5 and (R,C) in [(3,5), (5,3)]:
                    # Richard can pick a W shape
                    winner = Richard
                elif X == 6 and (R,C) in [(3,6), (6,3)]:
                    # Richard can pick a W shape
                    winner = Richard
                else:
                    # I think, Gabriel wins.
                    winner = Gabriel

    elif X >= 7:
        # Richard can choose an X-omino with a hole whose size is smaller than X,
        # so Gabriel is hooped.
        winner = Richard
    else:
        assert 0

    print 'Case #%d: %s' % (case_num, winner)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
