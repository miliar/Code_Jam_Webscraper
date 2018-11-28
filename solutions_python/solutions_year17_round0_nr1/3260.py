#!/usr/bin/env python3

from collections import deque

def bfs(s, k, m, n):
    visited = set()
    queue = deque([(s, 0)])

    while queue:
        v, c = queue.popleft()

        if v in visited:
            continue

        visited.add(v)

        for i in range(n - k + 1):
            r = v ^ (m << i)

            if r == (1 << n) - 1:
                return c + 1

            queue.append((r, c + 1))

    return -1

def solve(case):
    s, k = input().split(' ')
    k = int(k)
    n = len(s)
    s = int(s.replace('-', '0').replace('+', '1'), 2)
    m = (1 << k) - 1

    r = 0

    if s != (1 << n) - 1:
        r = bfs(s, k, m, n)

    print("Case #{}: {}".format(case + 1, r if r != -1 else 'IMPOSSIBLE'))

T = int(input())

for case in range(T):
    solve(case)
