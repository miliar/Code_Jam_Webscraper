#!/usr/bin/env python

import sys
from collections import defaultdict

def fix_min(d, k, v):
    if k in d:
        d[k] = min(d[k], v)
    else:
        d[k] = v

def fix_can(d, i, j, k):
    for n in range(k+1):
        d.setdefault(i+j+k, set()).add(n)

def precompute():
    cboring, csurp = {}, {}
    for i in range(11):
        for j in range(i, min(i+3, 11)):
            for k in range(j, min(i+3, 11)):
                if k - i <= 1:
                    fix_can(cboring, i, j, k)
                else:
                    fix_can(csurp, i, j, k)
    return cboring, csurp

def solve(funs):
    for no, line in enumerate(sys.stdin):
        if no == 0: continue # cases count
        result = solve_line(line.strip(), funs)
        print('Case #%d: %s' % (no, result))

def fits(score, psum, canset):
    return score in canset.get(psum, set())

def solve_line(line, funs):
    cboring, csurp = funs
    _n, s, p, *ts = map(int, line.split())
    result = 0
    for t in ts:
        fitsn = fits(p, t, cboring)
        fitss = fits(p, t, csurp)
        # print(s, p, t, fitsn, fitss)
        if fitsn:
            result += 1
        elif fitss and s > 0:
            result += 1
            s -= 1
    return result

def main():
    funs = precompute()
    # print(solve_line('3 3 7 17 11 21', funs))
    # print(solve_line('6 2 8 29 20 8 18 18 21', funs))
    solve(funs)

if __name__ == '__main__':
    main()
