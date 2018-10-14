#!/usr/bin/env python3
import sys

def testcase_gen(f):
    next(f) # skip num cases

    while True:
        smax, levels = next(f).split()

        yield int(smax), tuple(int(s) for s in levels)


def solve(smax, levels):
    standing_audience = 0
    added_friends = 0

    for shyness, num_people in enumerate(levels):
        if standing_audience < shyness:
            new_friends = shyness - standing_audience

            added_friends += new_friends
            standing_audience += new_friends

        standing_audience += num_people

    return added_friends

if __name__ == '__main__':
    testcases = testcase_gen(sys.stdin)
    for i, testcase in enumerate(testcases):
        print("Case #{}: {}".format(i+1, solve(*testcase)))
