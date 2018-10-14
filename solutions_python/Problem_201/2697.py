#!/usr/bin/python3

import sys
import math

def log2(x):
    return math.log(x)/math.log(.5)

def find_max(l):
    poses = []
    curmax = None

    for i in range(len(l)):
        if l[i] >= curmax or curmax == None:
            if l[i] > curmax:
                poses = []
            curmax = l[i]
            poses.append(i)
    return poses

cache = {}
def solve(data):
    N, K = [int(d) for d in data.split()]
    if (K, N) not in cache:
        stalls = [False] * N
        lefts = list(range(N))
        rights = list(range(N-1, -1, -1))
        for k in range(K):
            # print(lefts, rights, stalls)
            # find
            mins = [min(lefts[i], rights[i]) for i in range(N)]
            maxs = [max(lefts[i], rights[i]) for i in range(N)]
            keys = [(mins[i], maxs[i], -i) for i in range(N)]
            mk = max(keys)
            pos = -mk[2]

            # put
            stalls[pos] = True
            lefts[pos] = 0
            rights[pos] = 0
            for j in range(pos+1, N):
                lefts[j] = min(j - pos - 1, lefts[j])
            for j in range(0, pos):
                rights[j] = min(pos - j - 1, rights[j])
        cache[(K, N)] = (mk[1], mk[0])

    mx, mn = cache[(K, N)]
    return "{} {}".format(mx, mn)

    g = math.ceil((N+1) * 0.5 ** (math.ceil(log2(N/K)) - log2(N) + 0) - 2)
    return "{} {} {} {}".format(mk[1], mk[0], mk[1]-g, g)



T = int(sys.stdin.readline().strip())


for t in range(T):
    S = sys.stdin.readline().strip()
    print("Case #{}: {}".format(t+1, solve(S)))

