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

    (max_shyness, digits) = getline().split()
    max_shyness = int(max_shyness)

    assert len(digits) == max_shyness+1

    n_people_with_shyness_ = map(int, list(digits))

    n_people_standing = 0
    n_friends_I_need_to_invite = 0
    for s in range(0, max_shyness+1):
        mtrace('    %d people standing' % n_people_standing)
        mtrace('s=',s)
        # What do we have to do to get people with shyness s standing?
        npws = n_people_with_shyness_[s]
        mtrace('    %d people with shyness %d' % (npws, s))
        if npws == 0:
            # Nothing, there aren't any.
            pass
        else:
            # A person with shyness s will wait until at least s
            # other audience members have already stood up to clap,
            # and if so, she will immediately stand up and clap
            if n_people_standing >= s:
                # All these people will stand up
                mtrace('    they all stand up')
                n_people_standing += npws
            else:
                assert n_people_standing < s
                shortfall = s - n_people_standing
                mtrace('    I need to invite %d (more) friends' % shortfall)
                n_friends_I_need_to_invite += shortfall
                # And I can choose their shyness so that they're all
                # standing by this point.
                n_people_standing += shortfall
                mtrace('    so that there will instead be %d people standing' % n_people_standing)
                assert n_people_standing == s
                mtrace('    And that will make the %d people with shyness %d stand' % (npws, s))
                n_people_standing += npws
    mtrace('    %d people standing' % n_people_standing)
    assert n_people_standing == sum(n_people_with_shyness_) + n_friends_I_need_to_invite

    print 'Case #%d: %s' % (case_num, n_friends_I_need_to_invite)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
