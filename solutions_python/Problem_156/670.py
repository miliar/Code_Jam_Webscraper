import random
import sys

if len(sys.argv) == 1:
    sys.stdin = open(__file__.replace('.py', '.in'))
else:
    sys.stdin = open(sys.argv[1])
    sys.stdout = open(sys.argv[1].replace('.in', '') + '.out', 'w')

def get_ints():
    return map(int, raw_input().split())

n_cases = input()

def cost_for(plate_size, cutoff):
    return (plate_size + cutoff - 1) / cutoff - 1

assert cost_for(2, 10) == 0
assert cost_for(8, 2) == 3
assert cost_for(9, 2) == 4

for case in xrange(1, n_cases + 1):
    diner_count, = get_ints()
    plates = get_ints()

    min_time = max(plates)

    for min_size in xrange(2, min_time):
        cost = sum(cost_for(plate, min_size)
                   for plate in plates) + min_size
        min_time = min(min_time, cost)

    print "Case #%d: %s" % (case, min_time)
