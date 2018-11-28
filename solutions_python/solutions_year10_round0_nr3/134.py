#!/usr/bin/python

import sys

INPUT = sys.stdin
INPUT = open(sys.argv[1],'r')

def getline():
    return INPUT.readline()[:-1]

def trace(*strs):
    # if case_num != 10: return
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

def solve(n_runs, capacity, n_groups, size_of_group_):
    trace("n_runs =", n_runs)
    trace("capacity =", capacity)
    trace("n_groups =", n_groups)
    assert len(size_of_group_) == n_groups
    n_runs_so_far = 0
    n_euros_so_far = 0
    front_gi = 0
    memo_ = {}
    cycles_handled = False
    while True:
        if n_runs_so_far == n_runs:
            trace("and that's all the runs for the day")
            return n_euros_so_far
        trace()
        trace("run #", n_runs_so_far+1)
        trace("group at head of queue =", front_gi)

        if front_gi in memo_:
            (first_n_runs_so_far, first_n_euros_so_far, n_people_on_coaster_this_run, next_front_gi) = memo_[front_gi]
            if not cycles_handled:
                trace("cycle detected...")
                # The first time that group #front_gi was at the front of the queue,
                # there had been <first_n_runs_so_far> runs
                # and we had collected <first_n_euros_so_far> euros.
                cycle_n_runs = n_runs_so_far - first_n_runs_so_far
                cycle_n_euros = n_euros_so_far - first_n_euros_so_far
                trace("In each cycling, we'll do %d runs and collect %d euros" % (cycle_n_runs, cycle_n_euros))
                # How many times will we go around this cycle?
                n_cyclings = (n_runs - n_runs_so_far) / cycle_n_runs
                n_runs_in_cyclings = n_cyclings * cycle_n_runs
                n_euros_in_cyclings = n_cyclings * cycle_n_euros
                trace("In %d cyclings, we'll do %d runs and collect %d euros" % (n_cyclings, n_runs_in_cyclings, n_euros_in_cyclings))

                n_runs_so_far += n_runs_in_cyclings
                n_euros_so_far += n_euros_in_cyclings
                trace("So we've now done %d runs, collected %d euros" % (n_runs_so_far, n_euros_so_far))
                if n_runs_so_far == n_runs:
                    trace("and that's all the runs for the day")
                    return n_euros_so_far

                cycles_handled = True
                trace("")
                trace("run #", n_runs_so_far+1)
                trace("group at head of queue =", front_gi)

            trace("recall...")
        else:
            trace("sizes of groups in queue:", size_of_group_[front_gi:n_groups] + size_of_group_[0:front_gi])
            n_people_on_coaster_so_far = 0
            for gi in range(front_gi, n_groups) + range(0, front_gi):
                # can group gi ride?
                trace("  group %d has %d people. Can it ride?" % (gi,size_of_group_[gi]))
                if size_of_group_[gi] + n_people_on_coaster_so_far <= capacity:
                    # yes!
                    trace("    Yes!")
                    n_people_on_coaster_so_far += size_of_group_[gi]
                else:
                    trace("    No")
                    # No, they don't fit on this run.
                    # But they'll be at front of queue for next run.
                    next_front_gi = gi
                    break
            else:
                # no break from loop,
                # i.e., every group got to ride.
                assert sum(size_of_group_) <= capacity
                # This will be true of every run,
                # so the queue will never change.
                assert front_gi == 0
                next_front_gi = front_gi
            n_people_on_coaster_this_run = n_people_on_coaster_so_far

            # Whenever front_gi is at the front for a run,
            # n_people_on_coaster_this_run will ride, and
            # next_front_gi will be at the front for the next run.
            memo_[front_gi] = (n_runs_so_far, n_euros_so_far, n_people_on_coaster_this_run, next_front_gi)

        trace("so group %d is at front for next run" % next_front_gi)
        front_gi = next_front_gi
        trace("and this run leaves with %d people" % n_people_on_coaster_this_run)
        n_euros_so_far += n_people_on_coaster_this_run
        trace("euros so far today =", n_euros_so_far)
        n_runs_so_far += 1


n_cases = int(getline())
trace(n_cases,'cases:')
for case_num in range(1,n_cases+1):
    trace()
    trace( 'Case #', case_num )

    # R -> n_runs
    # k -> capacity
    # N -> n_groups
    (n_runs,capacity,n_groups) = map(int, getline().split())
    size_of_group_ = map(int, getline().split())

    n_euros = solve(n_runs,capacity,n_groups,size_of_group_)

    print 'Case #%d: %s' % (case_num, n_euros)
    sys.stdout.flush()

assert INPUT.readline() == ''

# vim: sw=4 ts=4 expandtab
