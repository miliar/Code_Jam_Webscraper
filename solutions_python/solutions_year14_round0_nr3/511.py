import sys

valid = None

def solvemine(r, c, m):
    """
Conditions for a board to be solvable in one click:
1) any cell adjacent to a mine must also be adjacent to a cell that is not adjacent to any mine.
2) there must be a contiguous region of cells not adjacent to any mines.

Edge cases:
1) board with only one non-mine cell is solvable in one click
2) board with only one row/column is always solvable unless all are mines
3) board with no mines is already solved

Strategy: take care of edge case first

Observations: 
1) if we can make a AxB area of empty cells inclusive of 0,0 where A>=2, B>=2, A<=R, B<=C, we're good
    """
    board = [['*' for j in range(c)] for i in range(r)]
    total = r*c
    empty = total-m
    if empty == 1:
        board[0][0] = 'c'
        return printboard(board)
    if m == 0:
        board = [['.' for j in range(c)] for i in range(r)]
        board[0][0] = 'c'
        return printboard(board)
    if r==1 or c==1:
        if m<total:
            board[0][0] = 'c'
            count = 1
            for i in range(r):
                for j in range(c):
                    if i==j and j==0: continue
                    if count==empty: return printboard(board)
                    board[i][j] = '.'
                    count += 1
        else:
            print "Impossible"
            return

    # brute force approach should work for small input
    board[0][0] = '.'
    board = expand(empty, board, 0, 0, 1)
    if not board:
        print "Impossible"
        return
    board[0][0] = 'c'
    return printboard(board)

def makevalidator(r, c):
    def validator(x,y):
        if x<0 or y<0 or x>=r or y>=c: return False
        return True

    return validator

def markboard(board, coord, mark):
    board[coord[0]][coord[1]] = mark

def getboard(board, coord):
    return board[coord[0]][coord[1]]

def expand(empty, b, x, y, currempty):
    """brute force recursive"""

    # try to surround self with empties
    fringe = []
    for nc in ( (x-1, y-1), (x, y-1), (x-1, y), (x+1, y+1), (x, y+1), (x+1, y), (x+1, y-1), (x-1, y+1) ):
        if valid(*nc) and getboard(b, nc)!='.':
            fringe.append(nc)
            markboard(b, nc, '.')
    newempty = currempty + len(fringe)
    if newempty==empty:
        return b
    if newempty>empty:
        for nc in fringe: markboard(b, nc, '*')
        return False

    for nc in fringe:
        res = expand(empty, b, nc[0], nc[1], newempty)
        if res: return res

    for nc in fringe: markboard(b, nc, '*')
    return False


def printboard(board):
    for r in board:
        print ''.join(r)

n = int(sys.stdin.readline())
for i in range(1,n+1):
    r,c,m = (int(val) for val in sys.stdin.readline().split())
    print "Case #%s:" % i
    valid = makevalidator(r,c)
    solvemine(r, c, m)

