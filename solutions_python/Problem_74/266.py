#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    return
    print >> sys.stderr, '..',
    for str in strs:
        print >> sys.stderr, str,
    print >> sys.stderr

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

    data = getline().split()
    trace( 'data: ', data )
    N = int(data[0])
    assert len(data) == 1 + 2*N

    last_seen_posn_and_time_ = {'O': (1,0), 'B': (1,0)}

    current_time = 0
    for i in range(N):
        botname = data[2*i + 1]
        button  = int(data[2*i + 2])
        trace()
        trace('command: bot', botname, ' push button', button)
        (last_seen_posn, last_seen_time) = last_seen_posn_and_time_[botname]
        trace('At t =', last_seen_time, 'bot was free at button', last_seen_posn)
        must_move = abs(button - last_seen_posn)
        trace('bot needed to move', must_move)
        t_finish_moving = last_seen_time + must_move
        trace('which would take till t =', t_finish_moving)
        if t_finish_moving < current_time:
            trace('then it had to wait till t =', current_time)
        else:
            current_time = t_finish_moving

        current_time += 1
        trace('then it pressed the button for 1 sec, till t =', current_time)
        last_seen_posn_and_time_[botname] = (button, current_time)

    print 'Case #%d: %s' % (case_num, current_time)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
