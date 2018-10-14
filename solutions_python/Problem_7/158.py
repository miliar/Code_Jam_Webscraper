#!/usr/bin/env python

from sys import argv

def is_in_grid(v1, v2, v3):
    x_r = (v1[0] + v2[0] + v3[0]) % 3
    y_r = (v1[1] + v2[1] + v3[1]) % 3
    if x_r == 0 and y_r == 0:
        #x = (v1[0] + v2[0] + v3[0]) / 3
        #y = (v1[1] + v2[1] + v3[1]) / 3
        #return [x, y] in grid
        return True
    else:
        return False

if __name__ == "__main__":
    fd = open(argv[1])
    N = int(fd.readline().strip())
    for q in range(N):
        n, A, B, C, D, x0, y0, M = [int(i) for i in fd.readline().split()]
        
        X = x0
        Y = y0
        grid = [[X, Y]]
        #print [X, Y]
        for  i in range(1, n):
            #print i
            X = (A * X + B) % M 
            Y = (C * Y + D) % M
            #print [X, Y]
            grid.append([X, Y])

        #print grid

        crop_triangles = 0

        grid.sort()
        grid_n = len(grid)
        for i in range(grid_n):
            v1 = grid[i]
            for j in range(i + 1, grid_n):
                v2 = grid[j]
                for k in range(j + 1, grid_n):
                    v3 = grid[k]
                    if is_in_grid(v1, v2, v3):
                        crop_triangles += 1

        print "Case #%d: %d" % (q + 1, crop_triangles)
                    
