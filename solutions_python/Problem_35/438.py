#!/usr/bin/env python

import sys
DEBUG = True

def solve(n):
    h, w = map(lambda x: int(x), raw_input().split(' '))
    valley = []
    basin = []
    parents = []
    children = []
    for i in range(h):
        valley.append(raw_input().split(' '))
        b = []
        p = []
        c = []
        for i in range(len(valley[-1])):
            b.append(99)
            p.append([[-1, -1]])
            c.append([-1, -1])
        basin.append(b)
        parents.append(p)
        children.append(c)
        
    basin[0][0] = 1
    basin_max = 1

    for i in range(h):
        v = valley[i]
        for j in range(len(v)):
            m = int(valley[i][j])
            di = -1
            dj = -1
            
            # north
            if (i - 1) >= 0:
                if int(valley[i-1][j]) < m:
                    m = int(valley[i-1][j])
                    di = i - 1
                    dj = j
            
            # west
            if (j - 1) >= 0:
                if int(valley[i][j-1]) < m:
                    m = int(valley[i][j-1])
                    di = i
                    dj = j - 1
            
            # east
            if (j + 1) < w:
                if int(valley[i][j+1]) < m:
                    m = int(valley[i][j+1])
                    di = i
                    dj = j + 1            
            
            # south
            if (i + 1) < h:
                if int(valley[i+1][j]) < m:
                    m = int(valley[i+1][j])
                    di = i + 1
                    dj = j
                
            if di > -1 and dj > -1:
                parents[di][dj].append([i, j])
                children[i][j] = [di, dj]

                if basin[i][j] == 99 and basin[di][dj] == 99:
                    basin_max += 1
                    basin[di][dj] = basin[i][j] = basin_max
                else:
                    if basin[di][dj] == 99:
                        basin[di][dj] = basin[i][j]
                    else:
                        a = basin[i][j]
                        b = basin[di][dj]
                        c = min(a, b)
                        basin[i][j] = basin[di][dj] = c
                        walks = []
                        
                        if c == b:
                            x, y = i, j
                        else:
                            x, y = di, dj

                        walks.extend(parents[x][y])
                        walks.append(children[x][y])
                            
                        while len(walks):
                            x, y = p = walks[0]
                            walks.remove(p)
                            if x == -1 and y == -1:
                                continue
                            basin[x][y] = c
                            if len(parents[x][y]) > 1:
                                walks.extend(parents[x][y])                                
                            
            else:
                if basin[i][j] == 99:
                    basin_max += 1
                    basin[i][j] = basin_max
        

    if not DEBUG:
        for va in valley:
            print va
        print '--'

    orders = []
    for i in range(len(basin)):
        v = basin[i]
        for j in range(len(v)):
            if basin[i][j] not in orders:
                orders.append(basin[i][j])
                
    orders.sort()
                
    for i in range(len(basin)):
        v = basin[i]
        for j in range(len(v)):
            valley[i][j] = chr(ord('a') + orders.index(basin[i][j]))
                    
    print 'Case #%d:' % n
    for v in valley:
        print ' '.join(v)

def main():
    t = int(raw_input())
    for i in range(1, t+1):
        solve(i)
    
if __name__ == '__main__':
    main()