#!/usr/bin/env python

import sys

infile = sys.stdin

T = int(infile.readline())

terrain = []

def comp_flow(y, x):
    min = val = terrain[y][x]
    flow = (y, x)
    for (dy, dx) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if 0 <= y + dy < H and 0 <= x + dx < W and terrain[y + dy][x + dx] < min:
            min = terrain[y + dy][x + dx]
            flow = (y + dy, x + dx)
    return flow

for case in range(1, T + 1):
    [H, W] = [int(x) for x in infile.readline().split()]

    terrain = []
    for y in range(H):
        terrain.append([int(h) for h in infile.readline().split()])
        
    flow = [[comp_flow(y, x) for x in range(W)] for y in range(H)] 

    queue = []
    id = 'a'
    chart = [['' for x in range(W)] for y in range(H)]

    for y0 in range(H):
        for x0 in range(W):
            if chart[y0][x0] != '':
                continue
            sink = (y0, x0)
            while (flow[sink[0]][sink[1]] != sink):
                sink = flow[sink[0]][sink[1]]

            queue.append(sink)
            while len(queue) > 0:
                (y, x) = queue.pop()
                chart[y][x] = id
                for (dy, dx) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if 0 <= y + dy < H and 0 <= x + dx < W:
                        if flow[y + dy][x + dx] == (y, x):
                            queue.append((y + dy, x + dx))
            id = chr(ord(id) + 1)

    print('Case #%d:' % case)
    for line in chart:
        for el in line:
            print el,
        print
