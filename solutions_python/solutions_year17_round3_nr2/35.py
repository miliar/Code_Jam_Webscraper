from math import ceil, floor, pi
import numpy as np
from functools import lru_cache


# @lru_cache(maxsize=None)
def get_min_switches(schedule):
    first_active = schedule[0][2]
    last_active = schedule[-1][2]
    last_end = schedule[-1][1] - 1440

    time_away = [0, 0]
    free_intervals = [[], []]
    switch_intervals = []

    prev_active = last_active
    prev_end = last_end
    for (start, end, person) in schedule:
        time_away[person] += end - start

        if prev_active == person:
            free_intervals[person] += [start - prev_end]
        else:
            switch_intervals += [start - prev_end]

        prev_active = person
        prev_end = end

    # print('free:', free_intervals)
    # print('switch:', switch_intervals)
    num_switches = len(switch_intervals)
    for p in [0, 1]:
        for t in sorted(free_intervals[p]):
            if time_away[p] + t <= 720:
                time_away[p] += t
            else:
                num_switches += 2

    return num_switches


if __name__=='__main__':
    PATH_IN = 'B-large.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline().split()
        num_a0 = int(line[0])
        num_a1 = int(line[1])
        print(num_a0, num_a1)

        start0 = np.zeros(num_a0)
        end0 = np.zeros(num_a0)
        start1 = np.zeros(num_a1)
        end1 = np.zeros(num_a1)
        schedule = []

        for i in range(num_a0):
            line = f_in.readline().split()
            start0[i] = int(line[0])
            end0[i] = int(line[1])
            schedule += [(start0[i], end0[i], 0)]

        for i in range(num_a1):
            line = f_in.readline().split()
            start1[i] = int(line[0])
            end1[i] = int(line[1])
            schedule += [(start1[i], end1[i], 1)]

        schedule = sorted(schedule)

        res = '%.i' % get_min_switches(schedule)

        print('Case #%i: %s' % (t+1, res))
        print()
        f_out.write('Case #%i: %s\n' % (t+1, res))
