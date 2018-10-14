#! /usr/bin/python3.1

import sys
import os
import itertools
import multiprocessing

def printworld(maxx, world):
    for number in world:
        for i in range(maxx, -1, -1):
            bit = "1" if number & (1 << i) else "0"
            sys.stdout.write(bit)
        sys.stdout.write("\n")
    sys.stdout.write("\n")
    return None

def solve(case):
    ncase, case = case
    print("Solving #{0}: {1}".format(ncase, case), file=sys.stderr)
    r, lines = case
    minx = miny = 1000001
    maxx = maxy = 0
    for x1, y1, x2, y2 in lines:
        minx = min(minx, x1)
        miny = min(miny, y1)
        maxx = max(maxx, x2)
        maxy = max(maxy, y2)
    lenx = maxx - minx + 1
    leny = maxy - miny + 1
    world = [0] * leny
    anyones = False
    for x1, y1, x2, y2 in lines:
        x1, x2 = x1 - minx, x2 - minx
        y1, y2 = y1 - miny, y2 - miny
        number = ((1 << ((x2 - x1) + 1)) - 1) << x1
        anyones = anyones or (number != 0)
        for i in range(y1, y2 + 1):
            world[i] |= number
    t = 0
    nworld = [0] * leny
    while anyones:
        anyones = False
        prev = 0
        for i, number in enumerate(world):
            next = (((number << 1) & prev) |
                    ((number << 1) & number) |
                    (number & prev))
            anyones = anyones or (next != 0)
            nworld[i] = next
            prev = number
        world, nworld = nworld, world
        t += 1
    return (ncase, t)

def read_cases(inf):
    ncases = int(inf.readline().strip())
    cases = []
    for i in range(1, ncases + 1):
        r = int(inf.readline().strip())
        lines = []
        for j in range(r):
            lines.append([int(x) for x in inf.readline().split()])
        case = (i, (r, lines))
        cases.append(case)
    return cases

def get_ncores():
    with open('/proc/cpuinfo') as f:
        cores = [x for x in f.readlines() if x.startswith('processor\t:')]
    return len(cores)

def main(argv=sys.argv):
    cases = read_cases(sys.stdin)
    pool = multiprocessing.Pool(processes=get_ncores())
    results = pool.map(solve, cases)
    #results = map(solve, cases)
    for i, result in results:
        print("Case #{0}: {1}".format(i, result))
    return 0
        
if __name__ == '__main__':
    sys.exit(main())
