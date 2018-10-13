from collections import *
from itertools import *

def solve(R, C, rs):
    sq = defaultdict(lambda: '.')
    sq.update(((r, c), rs[r][c]) for r,c in product(range(R), range(C)))
    for r, c in product(range(R), range(C)):
        if sq[(r,c)] == '#':
            if all(s == '#' for s in (sq[(r+1,c)], sq[(r,c+1)], sq[(r+1,c+1)])):
                sq[(r,c)] = '/'
                sq[(r+1,c)] = '\\'
                sq[(r,c+1)] = '\\'
                sq[(r+1,c+1)] = '/'
            else:
                return 'Impossible'
    return '\n'.join(''.join(sq[(r,c)] for c in range(C)) for r in range(R))

def main(L):
    i = 1
    for t in range(1, 1+int(L[0])):
        r, c = map(int, L[i].split())
        print 'Case #%d:\n%s' % (t, solve(r, c, [s.strip() for s in L[i+1:i+1+r]]))
        i += 1+r

import sys
main(list(sys.stdin))
