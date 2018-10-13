#!/usr/bin/env python3

"""
Alphabet Cake

Author: Alex Dale - @SuperOxigen
"""

import fileinput
import sys
from copy import deepcopy

def eprint(*args):
    print(*args, file=sys.stderr)

def findInitial(cake, initial):
    for r in range(len(cake)):
        for c in range(len(cake[r])):
            if cake[r][c] == initial:
                return r, c
    return -1, -1

def maxWidthFrom(cake, r, c, allowed) -> (int, str): # width, initial
    initial = None

    for col in range(c, len(cake[r])):
        if cake[r][col] != '?' and cake[r][col] not in allowed:
            return (col - c), initial
        if cake[r][col] != '?' and initial is None:
            initial = cake[r][col]
        elif cake[r][col] != '?':
            return (col - c), initial

    return len(cake[r]) - c, initial

def maxHeightFrom(cake, r, c, width, initial, allowed):
    for row in range(r+1, len(cake)):
        for col in range(c, c+width):
            if cake[row][col] != '?' and cake[row][col] not in allowed:
                return (row - r), initial
            if cake[row][col] != '?' and initial is None:
                initial = cake[row][col]
            elif cake[row][col] != '?':
                return (row - r), initial

    return len(cake) - r, initial

def findFirstOpen(cake, allowed):
    for row in range(len(cake)):
        for col in range(len(cake[row])):
            if cake[row][col] == '?' or cake[row][col] in allowed:
                return row, col
    return -1, -1

def sizePerm(width, height):
    sizes = []

    for w in range(1, width+1):
        for h in range(1, height+1):
            sizes.append((w, h))

    return sorted(sizes, key=lambda wh: -wh[0]*wh[1])

def widthPerm(width):
    return [i for i in range(1, width+1)]

def fillCake(cake, r, c, w, h, i):
    for row in range(r, h+r):
        for col in range(c, w+c):
            cake[row][col] = i

def qCount(cake):
    count = 0
    for row in cake:
        for col in row:
            if col == '?':
                count += 1
    return count

def initInRow(cake, r, c, width):
    for col in range(c, c+width):
        if cake[r][col] != '?':
            return cake[r][col]
    return None

def walkCake(cake, initials):
    if len(initials) == 0:
        return cake if qCount(cake) == 0 else None

    r, c = findFirstOpen(cake, initials)

    if r == -1:
        return None

    width, init = maxWidthFrom(cake, r, c, initials)

    if width == 0:
        return None

    for twidth in widthPerm(width):
        tinit = initInRow(cake, r, c, twidth)

        height, tinit = maxHeightFrom(cake, r, c, twidth, tinit, initials)

        if height == 0 or tinit is None:
            continue

        sizes = sizePerm(twidth, height)

        for size in sizes:
            w, h = size
            newCake = deepcopy(cake)
            inits = initials[:]
            inits.remove(tinit)
            fillCake(newCake, r, c, w, h, tinit)
            res = walkCake(newCake, inits)
            if res is not None:
                return res

    return None

def main():
    fin = fileinput.input()

    t = int(fin.readline().strip())

    for case in range(1, t+1):
        r, c = fin.readline().strip().split()
        r = int(r)
        c = int(c)

        cake = []
        initials = []

        for _ in range(r):
            row = list(fin.readline().strip())
            initials.extend([i for i in row if i != "?"])
            cake.append(row)

        res = walkCake(cake, initials)

        print("Case #{}:".format(case))
        if res is None:
            eprint("Did not work ({})".format(case))
            for row in cake:
                eprint("".join(row))
        else:
            for row in res:
                print("".join(row))


if __name__ == "__main__":
    main()
