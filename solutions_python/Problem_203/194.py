#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn)
    R, C = [int(x) for x in raw_input().split()]
    grid = [[x for x in raw_input()] for _ in xrange(R)]
    for i in xrange(R):
        j = 0
        while j < C:
            if grid[i][j] != '?':
                k = j - 1
                while k >= 0 and grid[i][k] == '?':
                    grid[i][k] = grid[i][j]
                    k -= 1
                k = j + 1
                while k < C and grid[i][k] == '?':
                    grid[i][k] = grid[i][j]
                    k += 1
                j = k - 1
            j += 1
    for j in xrange(C):
        i = 0
        while i < R:
            if grid[i][j] != '?':
                k = i - 1
                while k >= 0 and grid[k][j] == '?':
                    grid[k][j] = grid[i][j]
                    k -= 1
                k = i + 1
                while k < R and grid[k][j] == '?':
                    grid[k][j] = grid[i][j]
                    k += 1
                i = k - 1
            i += 1
    print '\n'.join([''.join(x) for x in grid])
