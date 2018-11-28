import sys
import re
from collections import deque

def solve(H, N, M, ceils, floors):
    cache = {}
    q0 = deque([(0, 0)])

    def go0(current, next):
        level = H
        cc = ceils[current[0]][current[1]]
        fc = floors[current[0]][current[1]]
        cn = ceils[next[0]][next[1]]
        fn = floors[next[0]][next[1]]
        if fc > cn - 50 or fn > cn - 50 or fn > cc - 50:
            # cannot enter, do nothing
            return
        if level <= cn - 50:
            # enter now.
            q0.append((next[0], next[1]))


    while len(q0) > 0:
        n, m = q0.popleft()
        if (n, m) in cache:
            continue
#        print('cache[({0}, {1})] <- {2}'.format(n, m, 0))
        if n > 0:
            go0((n, m), (n - 1, m))
        if m > 0:
            go0((n, m), (n, m - 1))
        if n + 1 < N:
            go0((n, m), (n + 1, m))
        if m + 1 < M:
            go0((n, m), (n, m + 1))
        cache[(n, m)] = 0
    q = deque()
    for (n, m) in cache:
        q.append((n, m, 0))
#        print('q <- ({0}, {1}, {2})'.format(n, m, 0))


    def go(q, current, next, t):
        level = H - t * 10
        cc = ceils[current[0]][current[1]]
        fc = floors[current[0]][current[1]]
        cn = ceils[next[0]][next[1]]
        fn = floors[next[0]][next[1]]
        if fc > cn - 50 or fn > cn - 50 or fn > cc - 50:
            # cannot enter, do nothing
            return
        if level <= cn - 50:
            # enter now.
            q.append((next[0], next[1], t + (1 if fc <= level - 20 else 10)))
        else:
            level_ = cn - 50
#            print('fc = {0}, fn = {1}, level_ = {2}'.format(fc, fn, level_))
            t_ = t + (level - level_) / 10
            q.append((next[0], next[1], t_ + (1 if fc <= level_ - 20 else 10)))

    cache = {}
    while len(q) > 0:
        n, m, t = q.popleft()
        if (n, m) in cache and cache[(n, m)] <= t:
            continue
        cache[(n, m)] = t
#        print('cache[({0}, {1})] <- {2}'.format(n, m, t))
        if n > 0:
            go(q, (n, m), (n - 1, m), t)
        if m > 0:
            go(q, (n, m), (n, m - 1), t)
        if n + 1 < N:
            go(q, (n, m), (n + 1, m), t)
        if m + 1 < M:
            go(q, (n, m), (n, m + 1), t)
    
    return cache[(N - 1, M - 1)]


T = int(sys.stdin.readline())

for i in range(T):
    H, N, M = [int(n) for n in sys.stdin.readline().split()]
    ceils = [[] for _ in range(N)]
    floors = [[] for _ in range(N)]
    for j in range(N):
        ceils[j] = [int(n) for n in sys.stdin.readline().split()]
    for j in range(N):
        floors[j] = [int(n) for n in sys.stdin.readline().split()]
        
    print('Case #{0}: {1}'.format(i + 1, solve(H, N, M, ceils, floors)))

