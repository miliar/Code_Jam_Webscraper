#!/usr/bin/python
# Using: Python 3.2.2

nr = int (input ())

for test_case in range (nr):
    case = [int (x) for x in input ().split (' ')]
    num_gog = case[0]
    num_trip = case[1]
    tscore = case[2]
    case = case[3:]
    assert num_gog == len (case)

    tscore_high = tscore + max ((tscore - 1), 0) * 2
    tscore_low =  tscore + max ((tscore - 2), 0) * 2
    result = 0
    for total in case:
        if total >= tscore_high:
            result += 1
        elif num_trip > 0 and total >= tscore_low:
            result += 1
            num_trip -= 1
    print ('Case #{}: {}'.format (test_case + 1, result))
