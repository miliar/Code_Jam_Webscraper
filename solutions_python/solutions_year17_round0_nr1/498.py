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
    # return
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

    (S, K) = getline().split()

    n_pancakes = len(S)
    flipper_length = int(K)
    assert 2 <= flipper_length <= n_pancakes

    pancakes = list(S)

    def flip(k):
        p = pancakes[k]
        if p == '+':
            flipped = '-'
        elif p == '-':
            flipped = '+'
        else:
            assert 0, p
        pancakes[k] = flipped

    n_flips = 0
    for i in range(0, n_pancakes):
        p = pancakes[i]
        if p == '+':
            # Pancake is happy side up.
            # No flipping needed.
            pass
        elif p == '-':
            # Pancake is blank side up.
            # Flip it and the flipper_length-1 pancakes to its right.
            try:
                for j in range(0, flipper_length): flip(i+j)
            except IndexError:
                result = 'IMPOSSIBLE'
                break
            n_flips += 1
        else:
            assert 0, p
        assert pancakes[i] == '+'
    else:
        result = n_flips

    print('Case #%d: %s' % (case_num, result))
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
