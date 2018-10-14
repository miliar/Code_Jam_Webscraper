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

    (R,C) = map(int, getline().split() )
    grid = []
    for r in range(R):
        row = getline()
        assert len(row) == C
        grid.append(list(row))
    trace('grid:')
    trace(grid)

    print 'Case #%d:' % (case_num)
    try:
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '.':
                    # fine
                    pass

                elif grid[r][c] == '#':
                    grid[r][c] = '/'

                    assert grid[r][c+1] == '#'
                    grid[r][c+1] = '\\'

                    assert grid[r+1][c] == '#'
                    grid[r+1][c] = '\\'

                    assert grid[r+1][c+1] == '#'
                    grid[r+1][c+1] = '/'

                elif grid[r][c] in ['/', '\\']:
                    # fine
                    pass

                else:
                    assert 0

        for r in range(R):
            print ''.join(grid[r])

    except (IndexError, AssertionError):
        print 'Impossible'

    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
