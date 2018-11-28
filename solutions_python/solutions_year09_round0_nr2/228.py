#!/usr/bin/python

import sys

def parent(idx, s):
    i, j = idx
    if s[i][j] == idx:
        return idx
    p = parent(s[i][j], s)
    s[i][j] = p
    return p

def join(s1, s2, s):
    i, j = parent(s1, s)
    p2 = parent(s2, s)
    s[i][j] = p2

def choose_next(y, x, map):
    num = map[y][x]
    lowest = (y, x)
    if y-1>=0 and map[y-1][x] < num:
        lowest = (y-1, x)
        num = map[y-1][x]
    if x-1>=0 and map[y][x-1] < num:
        lowest = (y, x-1)
        num = map[y][x-1]
    if x+1<len(map[y]) and map[y][x+1] < num:
        lowest = (y, x+1)
        num = map[y][x+1]
    if y+1<len(map) and map[y+1][x] < num:
        lowest = (y+1, x)
        num = map[y+1][x]
    i,j = lowest
    return lowest

def solve(map, h, w):
    solution_map = {}
    for i in range(h):
        solution_map[i] = {}
        for j in range(w):
            solution_map[i][j] = (i, j)
 
    for i in range(h):
        for j in range(w):
            lowest = choose_next(i, j, map)
            join((i, j), lowest, solution_map)
    known = {}
    next_letter = "a"
    solution = [0] * h
    for i in range(h):
        solution[i] = [0] * w
    for i in range(h):
        for j in range(w):
            p = parent((i, j), solution_map)
            if p not in known:
                known[p] = next_letter
                next_letter = chr(ord(next_letter) + 1)
            solution[i][j] = known[p]
    solution = "\n".join([" ".join(row) for row in solution])
    return solution

def main():
    n = int(raw_input())
    for i in range(1, n+1):
        h, w = map(int, raw_input().split())
        m = []
        for j in range(h):
            m.append(map(int, raw_input().split()))
        solution = solve(m, h, w)
        print "Case #%d:" % i
        print solution

if __name__ == "__main__":
    main()
    
                
