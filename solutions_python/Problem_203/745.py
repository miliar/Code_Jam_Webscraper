import sys, os, re, collections, heapq

def print_result (case_num, result):
    print('Case #{}: {}'.format(case_num + 1, result))

def solveLine (line):
    first = 0
    while line[first] == '?':
        first += 1
    c = line[first]
    r = []
    for a in line:
        if a == '?':
            r += [c]
        else:
            c = a
            r += [c]
    return r

def solve (grid):
    first = 0
    while not any([a != '?' for a in grid[first]]):
        first += 1
    l = solveLine(grid[first])
    r = []
    for line in grid:
        if all([a == '?' for a in line]):
            r += [''.join(l)]
        else:
            l = solveLine(line)
            r += [''.join(l)]
    return r

for case_num in range(int(input())):
    R,C = map(int,input().split())
    grid = []
    for r in range(R):
        grid.append(list(input()))
    r = solve(grid)
    print_result(case_num, '\n'+('\n'.join(r)))

