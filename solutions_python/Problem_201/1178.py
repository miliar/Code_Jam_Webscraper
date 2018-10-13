import fileinput
from queue import PriorityQueue
from functools import reduce
import math

def getLR(n):
    if n % 2 == 0:
        return n/2, n/2
    else:
        return (n+1)/2, (n-1)/2

def solve(N, K):
    # M = int(math.log2(N))
    # overhead = N - M
    # (pow(2, M) - 1) * pow(2^m)

    parts = PriorityQueue()
    parts.put((-N, N))
    for i in range(0, K):
        n = parts.get()[1]
        L, R = getLR(n)
        parts.put((-L, L))
        parts.put((-R, R))
        if i == K - 1:
            return int(L), int(R)

f = fileinput.input()
T = int(f.readline())
for case in range(1, T+1):
    N, K = map(int, f.readline().split())
    solution = solve(N, K)
    print("Case #{0}: {1} {2}".format(case, solution[0], solution[1]))
