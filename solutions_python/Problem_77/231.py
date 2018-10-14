#-*- encoding: utf-8 -*-
import sys

def solve(numbers):
    swap = 0
    state = [None] * (len(numbers)+1)
    for idx, n in enumerate(numbers):
        if idx+1 == n or state[n]:
            continue
        cur = n
        cycle_len = 0
        while state[cur] is None:
            cycle_len += 1
            state[cur] = 'Done'
            cur = numbers[cur-1]
        swap += cycle_len*1.0

    return float(swap)

if '__main__' == __name__:
    T = int(sys.stdin.readline().strip())
    for case_n in xrange(T):
        N = int(sys.stdin.readline().strip())
        numbers = map(int, sys.stdin.readline().strip().split())

        e_n = solve(numbers)
        print('Case #%d: %1.6f' % (case_n+1, e_n))
