from operator import mul
import sys


(WAIT_TOTAL,
 WAIT_CASE) = range(2)


def process_input():

    cases_count = 0

    state = WAIT_TOTAL
    for line in sys.stdin.readlines():
        line = line.strip()
        if line != '':

            if state == WAIT_TOTAL:
                c = long(line)
                state = WAIT_CASE
            elif state == WAIT_CASE:
                cases_count += 1
                assert cases_count <= c
                C, F, X = map(float, line.split(' '))
                ret = process_case(C, F, X)
                print 'Case #{}: {}'.format(cases_count, ret)
            else:
                assert False


def process_case(C, F, X):
    R = 2.0

    times = []
    targets = []
    xtimes = []
    sums = []
    f = 0
    while True:
        target = X + f * C
        current_rate = R + f * F
        time_to_next_farm = C / current_rate
        time_to_x = X / current_rate
        time_sum = sum(times) + time_to_x

        targets.append(target)
        times.append(time_to_next_farm)
        xtimes.append(time_to_x)
        if sums and time_sum > sums[-1]:
            return sums[-1]
        sums.append(time_sum)
        f += 1

    return 42.0  # Just in case !


if __name__ == '__main__':
    process_input()
