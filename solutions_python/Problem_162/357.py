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

level_for_target_ = {}

level_ = [set()]

level = 1
level_.append(set([1]))
level_for_target_[1] = 1

min_unreached = 2

while True:
    level += 1
    level_.append(set())

    mtrace('level', level)
    for prev_num in sorted(level_[level-1]):

        def reach( op, i ):
            mtrace('  ', prev_num, op, '=', i)
            if i in level_for_target_:
                # We already have a level for i,
                # and that level is necessarily <= this level
                mtrace('     ', i, 'is already at level', level_for_target_[i])
                pass
            else:
                mtrace('      ADDING', i, 'to this level')
                level_[level].add(i)
                level_for_target_[i] = level

        # you can either add one
        mtrace('  ', prev_num)
        reach( '+ 1', prev_num + 1 )
        # or you can reverse the digits
        reach( 'rev', int(''.join(reversed(list(str(prev_num))))) )

    while min_unreached in level_for_target_:
        min_unreached += 1

    mtrace('  min_unreached =', min_unreached)

    if min_unreached > 1000000:
        break

atrace('ready...')

n_cases = int(getline())
mtrace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    mtrace()
    atrace( 'Case #', case_num )

    N = int(getline())

    print 'Case #%d: %s' % (case_num, level_for_target_[N])
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
