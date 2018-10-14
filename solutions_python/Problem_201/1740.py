# codejam
from sys import stdin
from queue import *


def divide(m):
    if (m == 1):
        return 0, 0

    assert(m > 0)

    l = int((m - 1) / 2)
    return l, m - l - 1


# Solver
def solve(N, K):
    if (K > N * 0.8):
        return '0 0'

    q = PriorityQueue()
    q.put(-N)
    for i in range(0, K - 1):
        m = -q.get()
        if (m == 1):
            return '0 0'

        l, r = divide(m)
        q.put(-l)
        q.put(-r)

    l, r = divide(-q.get())

    return str(r) + ' ' + str(l)


# I/O
T = int(stdin.readline())

for t in range(0, T):
    N, K = [int(n) for n in stdin.readline().split(' ')]
    print('Case #{0}: {1}'.format(t + 1, solve(N, K)))
