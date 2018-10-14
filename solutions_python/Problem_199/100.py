import sys
from collections import deque


FLIP = {'-': '+', '+': '-'}


def compute(S, K):
    total_flips = 0
    flips = deque()
    next_c = '-'
    for i in xrange(len(S)):
        if S[i] == next_c:
            flips.append(i)
            next_c = FLIP[next_c]
            total_flips += 1
        if len(flips) > 0 and flips[0] + K <= i + 1:
            flips.popleft()
            next_c = FLIP[next_c]
    if len(flips) > 0:
        return "IMPOSSIBLE"
    return total_flips


def parse():
    S, K = sys.stdin.readline().strip().split()
    K = int(K)
    return S, K


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    count = 1
    part = 0
    if len(sys.argv) == 3:
        part = int(sys.argv[1])
        count = int(sys.argv[2])
    for i in xrange(T):
        data = parse()
        if i * count >= part * T and i * count < (part + 1) * T:
            result = compute(*data)
            print "Case #%d: %s" % (i + 1, result)
