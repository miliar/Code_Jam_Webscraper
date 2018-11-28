#! /usr/bin/env python


def operations_until_solvable(mote, prey_list, acc=0):
    # loser mote can't eat anything
    if mote == 1:
        return len(prey_list)

    if not prey_list:
        return acc
    prey = prey_list[0]
    if prey < mote:
        return operations_until_solvable(mote + prey, prey_list[1:], acc)
    return min(operations_until_solvable(mote + mote - 1, prey_list, acc + 1),
               operations_until_solvable(mote, prey_list[1:], acc + 1))

T = int(raw_input())

for case in xrange(T):
    A, N = map(int, raw_input().split())
    motes = map(int, raw_input().split())
    ans = operations_until_solvable(A, sorted(motes))
    print "Case #%d: %d" % (case + 1, ans)
