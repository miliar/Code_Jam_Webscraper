#!/usr/bin/env python3
def solve(h, w, f):
    for y in range(h):
        c = None
        for x in range(w):
            if f[y][x] != '?':
                c = f[y][x]
                break
        if c is None:
            f[y] = None
            continue
        for x in range(w):
            if f[y][x] == '?':
                f[y][x] = c
            else:
                c = f[y][x]
    for y in range(h-1):
        if f[y+1] is None and f[y] is not None:
            f[y+1] = list(f[y])
    for y in reversed(range(h-1)):
        if f[y] is None and f[y+1] is not None:
            f[y] = list(f[y+1])
    return f
t = int(input())
for x in range(t):
    h, w = map(int, input().split())
    f = [ list(input()) for _ in range(h) ]
    print('Case #{}:\n{}'.format(x+1, '\n'.join(map(''.join, solve(h, w, f)))))
