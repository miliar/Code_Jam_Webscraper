import sys
from collections import deque

def solve(R, gs):

    res = 0

    while R > 0:
        sum = 0
        cnt = 0
        while True:
            if sum + gs[0] <= k and cnt < len(gs):
                sum += gs[0]
                cnt += 1
                gs.append(gs.popleft())
            else:
                break
        R -= 1
        res += sum

    return res


T = int(raw_input())

for i in xrange(T):
    R, k, N = map(int, sys.stdin.readline().split(' '))
    gs = deque(map(int, sys.stdin.readline().split(' ')))

    print 'Case #%d: %d' % (i+1, solve(R, gs))
