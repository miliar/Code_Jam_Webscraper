from __future__ import absolute_import, division, print_function
import math
from collections import defaultdict

def solve_old(ac_schedules, aj_schedules):
    if sorted(ac_schedules)[0] < sorted(aj_schedules)[0]:
        ac = True
    else:
        ac = False
    both_free = True
    end = 0
    both_free_minutes = []
    ac_minutes = 0
    aj_minutes = 0
    changes = 0

    for i in range(0, 1440):
        if i in ac_schedules:
            if not ac:
                ac = not ac
                changes += 1
            end = ac_schedules[i]
        elif i in aj_schedules:
            if ac:
                ac = not ac
                changes += 1
            end = ac_schedules[i]

        if i == end:
            both_free = True

        if ac:
            ac_minutes += 1
        else:
            aj_minutes += 1

        if both_free:
            both_free_minutes.append(i)



def solve2(ac_schedules, aj_schedules):
    state = 'x'
    out= {}
    end = 0
    for i in range(0, 1440):
        if i in ac_schedules:
            state = 'c'
            end = ac_schedules[i]
        elif i in aj_schedules:
            state = 'j'
            end = aj_schedules[i]

        if i == end:
            state = 'x'

        out[i] = state

    start_state = ''
    end_state = ''
    if ac_schedules and aj_schedules:
        if sorted(ac_schedules)[0] < sorted(aj_schedules)[0]:
            start_state = 'C'
        else:
            end_state = 'J'
        if sorted(ac_schedules)[-1] < sorted(aj_schedules)[-1]:
            start_state = 'J'
        else:
            end_state = 'C'
    if not aj_schedules:
        start_state = 'C'
        end_state = 'C'
    if not ac_schedules:
        start_state = 'J'
        end_state = 'J'

    if not start_state or not end_state:
        raise Exception()

    for i in range(0, 1440):
        out[i] = start_state
        if i in ac_schedules or i in aj_schedules:
            break
    for i in range(1440, 0, -1):
        out[i] = end_state
        if i in ac_schedules or i in aj_schedules:
            break
    return out


def solve(aj, ac):
    if len(aj) < 2 and len(ac) < 2:
        return 2
    if len(aj) == 2:
        target = aj
    else:
        target = ac

    if len(target) ==1:
        return 2
    try:
        if target[0][0] > target[1][0]:
            target = [target[1], target[0]]
    except Exception:
        pass
    # could need 4:
    if abs(target[0][0] - target[1][1]) > 720:
        if abs(target[0][1] + (1440-target[1][0])) > 720:
            return 4
    return 2





#with open('Bsample.in') as f:
with open('B-small-attempt0.in') as f:
#with open('A-large.in') as f:
    T = int(f.readline())

    for puzzle_count in range(T):
        ac, aj = map(int, f.readline().strip().split(' '))
        #ac_schedules = {}
        # for i in range(0, ac):
        #     raw = f.readline().strip().split(' ')
        #     time_start, time_finish = map(int, raw)
        #     ac_schedules[time_start] = time_finish
        # aj_schedules = {}
        # for i in range(0, aj):
        #     raw = f.readline().strip().split(' ')
        #     time_start, time_finish = map(int, raw)
        #     aj_schedules[time_start] = time_finish
        ac_schedules = []
        for i in range(0, ac):
            raw = f.readline().strip().split(' ')
            time_start, time_finish = map(int, raw)
            ac_schedules.append((time_start, time_finish))
        aj_schedules = []
        for i in range(0, aj):
            raw = f.readline().strip().split(' ')
            time_start, time_finish = map(int, raw)
            aj_schedules.append((time_start, time_finish))

        ans = solve(ac_schedules, aj_schedules)

        print('Case #%s: %s' % (str(puzzle_count + 1), str(ans)))

