#!/usr/bin/python3

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
    print('..', end=' ', file=f)
    for str in strs:
        print(str, end=' ', file=f)
    print(file=f)
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

    N = getline()
    mtrace('N =',N)
    assert not N.startswith('0')

    n_digits = len(N)
    in_digits = list(map(int, list(N)))
    mtrace('in_digits =', in_digits)

    if sorted(in_digits) == in_digits:
        # N itself is tidy
        result = N
    else:
        # N is not tidy.
        # What is the highest tidy number less than N?

        # Find the leftmost point at which it turns untidy.
        for i in range(1, n_digits):
            if in_digits[i-1] <= in_digits[i]:
                # tidy so far
                pass
            else:
                untidy_posn = i
                break
        else:
            assert 0

        # split the digits of N into the tidy prefix and the rest:
        tidy_prefix_digits = in_digits[0:untidy_posn]
        remaining_digits = in_digits[untidy_posn:]

        # ----------

        # Neither part is empty:
        assert len(tidy_prefix_digits) > 0
        assert len(remaining_digits) > 0

        # and the tidy prefix is tidy:
        assert sorted(tidy_prefix_digits) == tidy_prefix_digits

        # and adding the next digit would not be tidy:
        test = tidy_prefix_digits + remaining_digits[0:1]
        assert sorted(test) != test

        # ----------

        out_digits = in_digits[:]

        # Move back to the left...
        for j in range(untidy_posn, 0, -1):
            if out_digits[j-1] <= out_digits[j]:
                # tidy transition, yay!
                assert j != untidy_posn
            else:
                assert out_digits[j-1] > 0
                out_digits[j-1] -= 1
                for k in range(j,n_digits): out_digits[k] = 9

        result = (''.join(map(str, out_digits))).lstrip('0')

    print('Case #%d: %s' % (case_num, result))
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
