#!/usr/bin/env pypy

testcases = int(raw_input())

for i in range(testcases):
    # Number of diners (throw away)
    inputline = raw_input()

    # List with all diners
    inputline = raw_input().rstrip()
    diners = map(lambda x: int(x), list(inputline.split()))

    # Observation 1: if we don't add any special minutes, the result
    # will be the maximum number of pancakes on a plate
    result = max(diners)

    # Now we try to add up more special minutes, till we find the optimal
    # result, which is defined by splitting up the plates
    special_minutes = 0
    while special_minutes < result:
        special_minutes += 1
        # When we start to split plates, the minimum is the number of
        # special_minutes we added +1 for the minute it takes to eat at least
        # one of the pancakes if everyone has just a single one after splitting
        new_result = special_minutes
        for plate in diners:
            new_result += (plate-1)/special_minutes
        result = min(result, new_result)
    print('Case #%d: %d' % (i + 1, result))
