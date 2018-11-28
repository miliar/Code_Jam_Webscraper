import sys
from itertools import combinations
rl = lambda: sys.stdin.readline().strip()

DIR = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def can_go(x, y, gx, gy, used, board, R, C, cnts):
    if x == gx and y == gy:
        return True
    used[x][y] = True
    for dx, dy in DIR:
        xx = x + dx
        yy = y + dy
        if xx < 0 or xx >= R or yy < 0 or yy >= C:
            continue
        if used[xx][yy]:
            continue
        if board[xx][yy] == '*':
            continue
        if cnts[xx][yy] != 0:
            continue
        if can_go(xx, yy, gx, gy, used, board, R, C, cnts):
            return True
    return False


def is_possible(R, C, board):
    if board[0][0] != '.':
        return False

    cnts = [[8 for c in range(C)] for r in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] == '*':
                continue
            cnt = 0
            for dx, dy in DIR:
                xx = x + dx
                yy = y + dy
                if xx < 0 or xx >= R or yy < 0 or yy >= C:
                    continue
                if board[xx][yy] == '*':
                    cnt += 1
            cnts[x][y] = cnt

    possible = True
    for x in range(R):
        for y in range(C):
            if board[x][y] == '*':
                continue

            if cnts[x][y] == 0:
                continue

            has_hero = False
            for dx, dy in DIR:
                xx = x + dx
                yy = y + dy
                if xx < 0 or xx >= R or yy < 0 or yy >= C:
                    continue

                if cnts[xx][yy] == 0:
                    has_hero = True
                    break

            if has_hero:
                continue
            else:
                possible = False
                break
    if possible:
        for x in range(R):
            for y in range(C):
                if board[x][y] == '.':
                    if not can_go(x, y, 0, 0, [[False for c in range(C)] for r in range(R)], board, R, C, cnts):
                        return False
        #for cnt in cnts:
        #    print ''.join(map(str, cnt))
    return possible


T = int(rl())
for tcase in range(T):
    R, C, M = map(int, rl().split())
    possible = False
    board = [['*' for c in range(C)] for r in range(R)]
    free = (R * C - M)

    RR, CC = R, C
    for RR in range(R, 0, -1):
        for CC in range(C, 0, -1):
            if RR * CC < free:
                continue

            board = [['*' for c in range(C)] for r in range(R)]
            for r in range(RR):
                for c in range(CC):
                    board[r][c] = '.'

            if free == 1:
                board = [['*' for c in range(C)] for r in range(R)]
                board[0][0] = '.'
                possible = True
                break

            r = RR - 1
            c = CC - 1
            r = r + 1 if r < 0 else r
            c = c + 1 if c < 0 else c

            remain_mine = RR * CC - free
            #print 'Case #%d' % (tcase + 1), remain_mine
            possible = True if is_possible(R, C, board) and remain_mine == 0 else False
            #print RR, CC, r, c, remain_mine
            if remain_mine > 0:
                hotspot = [(x, y) for y in range(c, CC) for x in range(0, RR)]
                hotspot += [(x, y) for y in range(0, CC) for x in range(r, RR)]
                hotspot = list(set(hotspot))
                #print hotspot
                possible = False
                for xys in combinations(hotspot, remain_mine):
                    for x, y in xys:
                        board[x][y] = '*'
                    possible = is_possible(R, C, board)
                    if possible:
                        break
                    for x, y in xys:
                        board[x][y] = '.'
            if possible:
                break
        if possible:
            break
    if possible:
        board[0][0] = 'c'
        cnt_mine = 0
        for row in board:
            cnt_mine += row.count('*')
        assert M == cnt_mine, 'fuck tcase(%d) %d != %d' % (tcase + 1, cnt_mine, M)
        print 'Case #%d:' % (tcase + 1)
        print '\n'.join([''.join(row) for row in board])
    else:
        print 'Case #%d:\nImpossible' % (tcase + 1)
