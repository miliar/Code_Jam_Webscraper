from string import lowercase
from copy import deepcopy
from qhd.dec import memoized
import sys

DIRECTIONS = ((-1,0), (0,-1), (0,1), (1,0))
def solve(map, H, W):
    if H == W == 1: return 'a'
    names = iter(lowercase)

    @memoized
    def sink(r,c):
        a, r1, c1 = min(
            (map[r+dr][c+dc], r+dr, c+dc)
            for dr,dc in DIRECTIONS
            if 0 <= r+dr < H and 0 <= c+dc < W
        )
        if map[r][c] <= a:
            return next(names)
        return sink(r1,c1)

    result = deepcopy(map)
    for r, row in enumerate(map):
        for c, col in enumerate(row):
            result[r][c] = sink(r,c)
    return '\n'.join(' '.join(col for col in row) for row in result)

f = sys.stdin
T = int(next(f))
for X in range(1, T+1):
    H, W = map(int, next(f).split())
    print 'Case #%d:' % X
    print solve([map(int, next(f).split()) for i in range(H)], H, W)
