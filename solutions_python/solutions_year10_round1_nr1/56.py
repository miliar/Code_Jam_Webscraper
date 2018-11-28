

import sys
stin = sys.stdin

t = int(stin.readline())

def iran(a, b=None):
    """Inclusive range."""
    if None == b:
        a, b = 0, a
    if b < a:
        return reversed(range(b, a+1))
    return range(a, b+1)

for tcase in range(1, t+1):
    n, k = map(int, stin.readline().split())
    board = []
    for i in range(n):
        board.append(list(stin.readline()))
    #for line in board:
    #    print ''.join(line)
    for row in range(n):
        for c in iran(n-1, 0):
            if '.' == board[row][c]:
                continue
            #Else move this one to the right.
            place = c
            for i in iran(c+1, n-1):
                if '.' != board[row][i]:
                    break
                place = i
            if place != c:
                board[row][place] = board[row][c]
                board[row][c] = '.'
    #for line in board:
    #    print ''.join(line)

    #Now determine.
    got = {'R': False, 'B' : False}
    for rstart in range(n):
        for cstart in range(n):
            if '.' == board[rstart][cstart]:
                continue
            looking_for = board[rstart][cstart]
            if got[looking_for]:
                continue
            if cstart + k <= n:
                full = True
                for x in iran(cstart+1, cstart+k-1):
                    if board[rstart][x] != looking_for:
                        full = False
                        break
                if True == full:
                    got[looking_for] = True
                    continue
            if rstart + k <= n:
                full = True
                for y in iran(rstart+1, rstart+k-1):
                    if board[y][cstart] != looking_for:
                        full = False
                        break
                if True == full:
                    got[looking_for] = True
                    continue
            if rstart + k <= n and cstart + k <= n:
                full = True
                for i in iran(1, k-1):
                    if board[rstart+i][cstart+i] != looking_for:
                        full = False
                        break
                if True == full:
                    got[looking_for] = True
                    continue
            if rstart + k <= n and cstart >= k-1:
                full = True
                for i in iran(1, k-1):
                    if board[rstart+i][cstart-i] != looking_for:
                        full = False
                        break
                if True == full:
                    got[looking_for] = True
                    continue
                
    print "Case #%d:" % tcase,
    if got['R'] and got['B']:
        print "Both"
    elif got['R']:
        print "Red"
    elif got['B']:
        print "Blue"
    else:
        print "Neither"

