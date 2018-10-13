#!/usr/bin/env python

from sys import stdin

T = int(stdin.readline())
for t in range(T):
    # Phase 0: read height map
    (H, W) = map(int, stdin.readline().split(' '))
    M = [ map(int, stdin.readline().split(' ')) for r in range(H) ]

    # Phase 1: for each cell, identify the cell water flows to
    T = [ [ None ]*W for r in range(H) ]
    for r in range(H):
        for c in range(W):
            br, bc = r, c
            for dr, dc in [ (-1, 0), (0, -1), (0, 1), (1, 0) ]:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < H and nc >= 0 and nc < W \
                    and M[nr][nc] < M[br][bc]: br,bc = nr,nc
            if (br,bc) != (r, c): T[r][c] = br,bc

    # Phase 2: label cells
    L = [ [ None ]*W for r in range(H) ]
    labels = 0
    for r in range(H):
        for c in range(W):
            nr,nc = r,c
            cells = [ ]
            while L[nr][nc] is None:
                if T[nr][nc] is None:
                    # Label sink
                    assert labels < 26
                    L[nr][nc] = chr(ord('a') + labels)
                    labels += 1
                else:
                    # Follow stream
                    cells.append((nr, nc))
                    nr,nc = T[nr][nc]

            label = L[nr][nc]
            for (nr,nc) in cells: L[nr][nc] = label

    print 'Case #' + str(t + 1) + ':'
    for row in L: print ' '.join(row)
