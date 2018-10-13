#!/usr/bin/python

import sys
from collections import defaultdict

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

    (N,K) = map(int, getline().split())
    assert 1 <= K <= N

    # We're interested in spans of unoccupied stalls.
    spans = defaultdict(int)
    # spans[k] will be the number of spans of length k
    spans[N] = 1

    n_people_so_far = 0
    while True:
        mtrace()
        max_span_length = max(spans.keys())
        mtrace('max_span_length =', max_span_length)
        assert max_span_length > 0
        n_spans_of_max_length = spans[max_span_length]
        mtrace('n_spans_of_max_length =', n_spans_of_max_length)
        # So the next `n_spans_of_max_length` people
        # will pick one of those spans
        # (the leftmost, though that doesn't matter),
        # and then enter the stall at (or left-adjacent to) its middle.

        # In each case, this will create two smaller spans:
        if max_span_length % 2 == 1:
            # There's a stall in the exact middle
            L_span_length = R_span_length = (max_span_length-1) / 2
        else:
            # There's a stall either side of the exact middle.
            # The person will choose the left one of the two,
            # so the resulting left-span will be
            # 1 shorter than the resulting right-span.
            R_span_length = max_span_length / 2
            L_span_length = R_span_length - 1

        # Note that L_span_length and R_span_length are exactly the values
        # of Ls and Rs in the problem statement.

        mtrace('L_span_length =', L_span_length, '  R_span_length =', R_span_length)
        # Is the K'th person in this cohort of people?
        assert K > n_people_so_far
        if K <= n_people_so_far + n_spans_of_max_length:
            # Yes, they are.
            # y = max(Ls, Rs); z = min(Ls, Rs)
            y = max(L_span_length, R_span_length)
            z = min(L_span_length, R_span_length)
            break
        else:
            # No they aren't.
            # So compute the effect of this cohort.
            # All the spans of this length will be used...
            n_people_so_far += n_spans_of_max_length
            del spans[max_span_length]
            # ... and each will be replaced with two shorter spans:
            spans[L_span_length] += n_spans_of_max_length
            spans[R_span_length] += n_spans_of_max_length

        assert len(spans) <= 4

    print 'Case #%d: %s %s' % (case_num, y, z)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
