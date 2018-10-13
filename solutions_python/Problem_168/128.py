import sys
rl = lambda: sys.stdin.readline().strip()
dirs = {'>': (0, 1),
        '<': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)}
R, C = None, None


def is_safe(x1, board):
    x, y, d = x1
    x += dirs[d][0]
    y += dirs[d][1]
    while True:
        if x < 0 or y < 0 or x >= R or y >= C:
            return False
        if board[x][y] in dirs:
            return True
        x += dirs[d][0]
        y += dirs[d][1]


T = int(rl())
for tcase in range(1, T + 1):
    print >> sys.stderr, tcase
    R, C = map(int, rl().split())
    board = [[c for c in rl()] for r in range(R)]
    pos = []
    for r in range(R):
        for c in range(C):
            if board[r][c] in ['>', '<', 'v', '^']:
                pos.append((r, c, board[r][c]))
    can = True
    pos.sort(key=lambda x: (x[0], x[1]))
    for x1 in pos:
        dd = sum([1 for x2 in pos if x1[0] == x2[0]]) + sum([1 for x2 in pos if x1[1] == x2[1]])
        if dd < 3:
            can = False
    if not can:
        print 'Case #%d: IMPOSSIBLE' % tcase
        continue
    ans = 0
    for x1 in pos:
        if is_safe(x1, board):
            continue
        nearest = None
        dist = 9887654321
        for x2 in pos:
            if x1 == x2:
                continue
            dd = None
            if x1[0] == x2[0]:
                dd = abs(x1[1] - x2[1])
            if x1[1] == x2[1]:
                dd = min(dd, abs(x1[0] - x2[0]))
            if dd and dd < dist:
                dist = dd
                nearest = x2
        if x1[0] == x2[0]:
            board[x1[0]][x1[1]] = '>' if x1[1] < x2[1] else '<'
        elif x1[1] == x2[1]:
            board[x1[0]][x1[1]] = 'v' if x1[0] < x2[0] else '^'
        ans += 1
    print 'Case #%d: %d' % (tcase, ans)
