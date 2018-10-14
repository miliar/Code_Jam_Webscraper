#!/usr/bin/env pypy

# IN_FILE = 'sample.in'
# IN_FILE = 'B-small-attempt0.in'
IN_FILE = 'B-large.in'
fp = open(IN_FILE, 'r')

NUM_TESTS = int(fp.readline())
TESTS = []
for i in range(NUM_TESTS):
    line = fp.readline().strip().split(' ')
    c, f, x = float(line[0]), float(line[1]), float(line[2])
    TESTS.append({
        'C': c,
        'F': f,
        'X': x,
    })
fp.close()

# from pprint import pprint
# pprint(TESTS)


def solve(C, F, X):
    if C >= X:
        return X / 2.0

    curr_rate = 2.0
    curr_time = C / 2.0
    while True:
        # current money is always C at this point
        # to decide whether I should buy a new farm?

        # without buying a new farm
        time1 = curr_time + (X - C) / curr_rate

        # if by a new farm
        time2 = curr_time + X / (curr_rate + F)

        if time1 < time2:
            return time1

        curr_rate += F
        curr_time += C / curr_rate


for i in range(NUM_TESTS):
    test = TESTS[i]
    res = solve(test['C'], test['F'], test['X'])
    print 'Case #%d:' % (i + 1),
    print '%.7f' % res
