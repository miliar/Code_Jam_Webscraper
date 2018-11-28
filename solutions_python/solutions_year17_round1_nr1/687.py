#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import sys
import math

def next_in_line(i, j, grid):
    if j >= C:
        return (j, '?')
    while grid[i][j] == '?':
        j +=1
        if j >= C:
            return (j, '?')
    return (j, grid[i][j])
    

with open(sys.argv[1], 'r') as f:
    for n in range(int(f.readline())):
        R, C = [int(i) for i in f.readline().split()]
        grid = [[c for c in f.readline()] for i in range(R)]
        i = 0
        j = 0
        letter = '?'
        for i in range(R):
            j=0
            (j1, letter) = next_in_line(i, j, grid)
            #fill left
            for j2 in range(j, j1+1):
                grid[i][j2] = letter
            #fill right
            j = j1
            (j1, letter1) = next_in_line(i, j+1, grid)
            while j1 <= C:
                for j2 in range(j, min(j1,C)):
                    grid[i][j2] = letter
                letter = letter1
                j = j1
                (j1, letter1) = next_in_line(i, j1+1, grid)

        for i in range(R):
            if '?' in grid[i]:
                i1 = i
                while i1 >=0 and '?' in grid[i1]:
                    i1 -=1
                if i1<0:
                    i1 = i
                    while i1 < R and '?' in grid[i1]:
                        i1 += 1
                grid[i] = grid[i1]
        print("Case #"+str(n+1)+":")
        for i in range(R):
            print ''.join(grid[i][:-1])
