#! /usr/bin/python3.1

import sys
import os
import itertools
import multiprocessing

RESULTS = ['Neither', 'Blue', 'Red', 'Both']

def tr(n, x, y):
    return (y * n) + x

def check_horiz(n, k, rot, c):
    for y in range(n):
        count = 0
        for x in range(n):
            if rot[tr(n, x, y)] == c:
                count += 1
                if count == k:
                    return True
            else:
                count = 0
    return False
    
def check_vert(n, k, rot, c):
    for x in range(n):
        count = 0
        for y in range(n):
            if rot[tr(n, x, y)] == c:
                count += 1
                if count == k:
                    return True
            else:
                count = 0
    return False

def check_diag1(n, k, rot, c):
    for y in range(n - 1, 0, -1):
        x = 0
        count = 0
        while x < n and y < n:
            if rot[tr(n, x, y)] == c:
                count += 1
                if count == k:
                    return True
            else:
                count = 0
            x += 1
            y += 1
    for x in range(n):
        y = 0
        count = 0
        while x < n and y < n:
            if rot[tr(n, x, y)] == c:
                count += 1
                if count == k:
                    return True
            else:
                count = 0
            x += 1
            y += 1
    return False

def check_diag2(n, k, rot, c):
    for y in range(n - 1, 0, -1):
        x = n - 1
        count = 0
        while x >= 0 and y < n:
            if rot[tr(n, x, y)] == c:
                count += 1
                if count == k:
                    return True
            else:
                count = 0
            x -= 1
            y += 1
    for x in range(n - 1, -1, -1):
        y = 0
        count = 0
        while x >= 0 and y < n:
            if rot[tr(n, x, y)] == c:
                count += 1
                if count == k:
                    return True
            else:
                count = 0
            x -= 1
            y += 1
    return False

def check_all(n, k, rot, c):
    return (check_horiz(n, k, rot, c) or check_vert(n, k, rot, c) or
            check_diag1(n, k, rot, c) or check_diag2(n, k, rot, c))
    
def solve(case):
    ncase, case = case
    print("Solving #{0}".format(ncase), file=sys.stderr)
    n, k, lines = case
    rot = [None] * (n*n)
    for r in range(n):
        y = n - 1
        for c in range(n - 1, -1, -1):
            v = lines[r][c]
            if v == '.':
                continue
            rot[tr(n, n - r - 1, y)] = v
            y -= 1
    blue = 1 if check_all(n, k, rot, 'B') else 0
    red = 1 if check_all(n, k, rot, 'R') else 0
    return (ncase, RESULTS[blue | (red << 1)])

def read_cases(inf):
    ncases = int(inf.readline().strip())
    cases = []
    for i in range(1, ncases + 1):
        n, k = [int(x) for x in inf.readline().split()]
        lines = []
        for j in range(n):
            lines.append(inf.readline())
        case = (i, (n, k, lines))
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
    #results = [solve(case) for case in cases]
    for i, result in results:
        print("Case #{0}: {1}".format(i, result))
    return 0
        
if __name__ == '__main__':
    sys.exit(main())
