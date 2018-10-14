#!/usr/bin/python3
import itertools


for test_case in range(int(input())):
    print('Case #{}: '.format(test_case + 1), end='')
    cost, bonus, to_win = map(float, input().split())
    best = 1e100
    time_passed = 0
    for farms_count in itertools.count(0):
        current = time_passed + to_win / (2.0 + bonus * farms_count)
        if current < best:
            best = current
        else:
            break
        time_passed += cost / (2.0 + bonus * farms_count)
    print('{:.7f}'.format(best))