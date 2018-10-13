#!/usr/bin/python3.4

import sys
import math

# array[r][c]

ht = {'^': (-1, 0),
      '>': ( 0, 1),
      '<': ( 0,-1),
      'v': ( 1, 0)}

arrows = '^><v'

def valid(ri, ci):
    if ri < 0:
        return False
    if ri >= r:
        return False
    if ci < 0:
        return False
    if ci >= c:
        return False
    return True

def follow(ri, ci):
    d = ht[array[ri][ci]]

    while True:
        ri += d[0]
        ci += d[1]

        if not valid(ri, ci):
            return None

        if array[ri][ci] != '.':
            break

    return (ri, ci)

def get_next(r):
    p = arrows.find(r)
    if p == -1:
        return
    return arrows[(p+1)%4]

# Return nb changes
def fix(ri, ci):
    global good
    global visited
    changed = 0

    if good[ri][ci]:
        return 0

    if visited[ri][ci]:
        return 0

    visited[ri][ci] = True

    n = follow(ri, ci)

    # Make it point to an other arrow
    if n==None:
        changed += 1

        done = False
        for i in range(3):
            c = array[ri][ci]
            c = get_next(c)
            array[ri][ci] = c

            n = follow(ri, ci)
            if n != None:
                done = True
                break

        if done == False:
            return None

    f = fix(n[0], n[1])
    if f==None:
        return None

    changed += f

    good[ri][ci] = True

    return changed

def solve():
    global visited
    global good
    nb_changes = 0

    good = [ [ False for i in range(c) ] for j in range(r) ]

    for ri in range(r):
        first = -1
        for ci in range(c):
            if array[ri][ci] != '.':
                first = ci

        if first == -1:
            continue

        visited = [[ False for i in range(c) ] for j in range(r)]
        nb = fix(ri, first)
        if nb == None:
            return 'IMPOSSIBLE'
        nb_changes += nb

        for ci in reversed(range(c)):
            if array[ri][ci] != '.':
                first = ci

        nb = fix(ri, first)
        if nb == None:
            return 'IMPOSSIBLE'
        nb_changes += nb

    for ci in range(c):
        first = -1
        for ri in range(r):
            if array[ri][ci] != '.':
                first = ri

        if first == -1:
            continue

        visited = [[ False for i in range(c) ] for j in range(r)]
        nb = fix(first, ci)
        if nb == None:
            return 'IMPOSSIBLE'
        nb_changes += nb

        for ri in reversed(range(r)):
            if array[ri][ci] != '.':
                first = ri

        nb = fix(first, ci)
        if nb == None:
            return 'IMPOSSIBLE'
        nb_changes += nb

    return nb_changes

def main():
    global r, c
    global array

    nb = int(get_line())
    for case_id in range(1, nb + 1):
        r, c = [int(a) for a in get_line().split()]
        array  = [list(get_line()) for a in range(r)]

        ret = solve()

        print('Case #%d: %s' % (case_id, ret), file = o)

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

