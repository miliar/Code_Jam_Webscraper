from __future__ import division

import math

num_tests = input()

for i in range(0, num_tests):
    gaps = {}
    data = raw_input().split()
    num_mics = int(data[0])
    num_people = int(data[1])

    gaps[num_mics] = 1
    for j in range(0, num_people):
        max_gap = max(gaps, key = int)

        high = math.ceil((max_gap - 1) / 2)
        low = math.floor((max_gap - 1) / 2)

        if j == num_people - 1:
            print 'Case #' + str(i+1) + ': ' + str(int(high)) + ' ' + str(int(low))
            break

        gaps[max_gap] -= 1
        if gaps[max_gap] == 0:
            del gaps[max_gap]

        if high in gaps:
            gaps[high] += 1
        else:
            gaps[high] = 1
        if low in gaps:
            gaps[low] += 1
        else:
            gaps[low] = 1
