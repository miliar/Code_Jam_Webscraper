#!/usr/bin/env python2.7

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
}
IMPOSSIBLE = 'IMPOSSIBLE'

T = int(raw_input())
for x in xrange(1, T + 1):
    R, C = map(int, raw_input().split())
    board = [raw_input().strip() for i in xrange(R)]
    def is_bad(r, c, d):
        y, x = r + d[0], c + d[1]
        while 0 <= y < R and 0 <= x < C:
            if board[y][x] != '.':
                return False
            y, x = y + d[0], x + d[1]
        else:
            return True
    res = 0
    for r in xrange(R):
        for c in xrange(C):
            if res == IMPOSSIBLE:
                break
            if board[r][c] == '.':
                continue
            if is_bad(r, c, dirs[board[r][c]]):
                for d in dirs.values():
                    if not is_bad(r, c, d):
                        break
                else:
                    res = IMPOSSIBLE
                    break
                res += 1
    print 'Case #{}: {}'.format(x, res)
