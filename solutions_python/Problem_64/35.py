#!/usr/bin/env python
#-*- encoding: utf-8 -*-

from pprint import pprint

import psyco
psyco.full()

def bit(n, b):
    return (n >> b) & 1

def read_grid(M):
    grid = []
    for m in xrange(M):
        l = raw_input()
        l = [int(c, 16) for c in l]
        a = []
        for n in l:
            for i in xrange(3, -1, -1):
                a.append(bit(n, i))
        grid.append(a)
    return grid

def in_grid(M, N, (x, y)):
    return (0 <= x < N) and (0 <= y < M)

def compute_adj(M, N, G, delta):
    dx, dy = delta
    adj = [[0] * N for m in xrange(M)]
    for y in xrange(M):
        for x in xrange(N):
            count = 0
            cont = True
            if adj[y][x]:
                continue # already done
            nx, ny = x, y
            while cont:
                count += 1
                nnx, nny = nx + dx, ny + dy
                cont = in_grid(M, N, (nnx, nny)) and (G[ny][nx] != G[nny][nnx])
                nx, ny = nnx, nny
            nx, ny = x, y
            i = count
            while i > 0:
                adj[ny][nx] = i
                i -= 1
                nx, ny = nx + dx, ny + dy
    return adj

def all_sized(M, N, adj):
    for s in xrange(min(M, N), 0, -1):
        for y in xrange(M):
            for x in xrange(N):
                if adj[y][x] == s:
                    yield (x, y)

def solve(t, M, N, inter, right, bottom):
    squares = [0] * N
    nsizes = 0
    for (x, y) in all_sized(M, N, inter):
        s = inter[y][x]
        try:
            for i in xrange(s):
                if right[y + i][x] < s:
                    raise ValueError
                elif bottom[y][x + i] < s:
                    raise ValueError
                for j in xrange(s):
                    if not inter[y + i][x + j]:
                        raise ValueError
        except ValueError:
            inter[y][x] -= 1
            continue
        if squares[s] == 0:
            nsizes += 1
        squares[s] += 1
        for i in xrange(s):
            for j in xrange(s):
                inter[y + i][x + j] = 0
    print 'Case #%d: %d' % (t, nsizes)
    for s, n in reversed(list(enumerate(squares))):
        if n == 0: continue
        print '%d %d' % (s, n)

T = input()
for t in xrange(1, T+1):
    M, N = [int(x) for x in raw_input().split()]
    G = read_grid(M)
    bottom = compute_adj(M, N, G, (0, 1))
    right = compute_adj(M, N, G, (1, 0))
    inter = [[min(bottom[y][x], right[y][x]) for x in xrange(N)] for y in xrange(M)]
    solve(t, M, N, inter, right, bottom)
