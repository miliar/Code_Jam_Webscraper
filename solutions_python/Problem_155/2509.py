#!/usr/bin/env python2

def solve(d):
    answer, stand = 0, 0
    for shy, j in enumerate(d):
        diff = max(0, shy - stand)
        answer += diff
        stand += diff + j
    return answer

N = input()
for i in range(1, N + 1):
    print 'Case #{0}: {1}'.format(i, solve([int(x) for x in raw_input().split()[1]]))
