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

    rowA = int(getline())
    rowA_ = []
    for i in range(4):
        rowA_.append( getline().split() )
    rowB = int(getline())
    rowB_ = []
    for i in range(4):
        rowB_.append( getline().split() )

    mtrace(rowA, rowA_, rowB, rowB_)

    possiblesA = set(rowA_[rowA-1])
    possiblesB = set(rowB_[rowB-1])

    mtrace(possiblesA, possiblesB)

    intersection = set.intersection(possiblesA, possiblesB)
    mtrace(intersection)
    if len(intersection) == 0:
        result = 'Volunteer cheated!'
    elif len(intersection) == 1:
        result = intersection.pop()
    else:
        result = 'Bad magician!'

    print 'Case #%d: %s' % (case_num, result)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
