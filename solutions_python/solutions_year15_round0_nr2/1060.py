
import sys

Cache = {}

def time_till_done(stacks):
    if not stacks: return 0
    stacks = [x for x in stacks if x]
    stacks.sort(reverse = True)

    if stacks[0] == 0:
        return 0
    if stacks[0] == 1:
        return 1

    tstacks = tuple(stacks)
    if tstacks in Cache:
        return Cache[tstacks]

    original_max = stacks[0]
    best_so_far = original_max

    # try different divisions of those pancakes
    for div in xrange(1, original_max//2 + 1):
        new_stacks = stacks[:]
        new_stacks[0] = div
        new_stacks.append(original_max - div)
        best_so_far = min(best_so_far, 1 + time_till_done(new_stacks))

    Cache[tstacks] = best_so_far
    return best_so_far


def read_line():
    return sys.stdin.readline().strip()


num_cases = int(read_line())
for casenum in xrange(num_cases):
    read_line()
    stacks = [int(x) for x in read_line().split(" ")]

    Cache.clear()
    print "Case #%d: %d" % (casenum + 1, time_till_done(stacks))

