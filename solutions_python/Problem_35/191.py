#!/usr/bin/env python

import sys
import string

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()

    T = int(lines[0].strip())

    base = 1
    for case in range(T):
        H, W = map(int, lines[base].strip().split())
        t = []
        for i in range(H):
            t.append(map(int, lines[base+i+1].strip().split()))

        base += 1 + H
        solution = solve(t, W, H)
        print "Case #%d:" % (case+1)
        for line in solution:
            print ' '.join(line)

def solve(t, W, H):
    soln = []
    for i in range(H):
        soln.append([None] * W)

    letter = 0
    for i in range(H):
        for j in range(W):
            if flows_to(t, i, j, W, H) == None:
                soln[i][j] = letter
                letter += 1

    for i in range(H):
        for j in range(W):
            if soln[i][j] == None:
                soln[i][j] = find_letter(soln, t, i, j, W, H)

    seen_letters = []

    for i in range(H):
        for j in range(W):
            try:
                idx = seen_letters.index(soln[i][j])
            except:
                idx = len(seen_letters)
                seen_letters.append(soln[i][j])
            soln[i][j] = string.lowercase[idx]

    return soln

def find_letter(soln, t, i, j, W, H):
    a, b = flows_to(t, i, j, W, H)
    if soln[a][b] == None:
        return find_letter(soln, t, a, b, W, H)
    else:
        return soln[a][b]

def flows_to(t, i, j, W, H):
    possible = []
    if i < H-1:
        possible.append((t[i+1][j], 3, i+1, j))
    if j < W-1:
        possible.append((t[i][j+1], 2, i, j+1))
    if i > 0:
        possible.append((t[i-1][j], 0, i-1, j))
    if j > 0:
        possible.append((t[i][j-1], 1, i, j-1))

    possible.sort()

    if len(possible):
        if possible[0][0] < t[i][j]:
            return (possible[0][2], possible[0][3])
        else:
            return None

if __name__ == '__main__':
    main()