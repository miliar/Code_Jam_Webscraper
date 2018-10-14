import sys
input = open(sys.argv[1], 'r')

for i in range(int(input.readline())):
    board = []
    for _ in range(4):
        board.append(list(input.readline().strip()))
    input.readline()

    def lookDir(row, col, func, look):
        seen = 0
        while 0 <= col < 4 and 0 <= row < 4:
            c = board[row][col]
            if c in [look, 'T']: seen += 1
            else: return False
            row, col = func(row, col)
        return seen == 4

    def checkWin(look):
        win = False
        for m in range(len(board)):
            win = lookDir(m, 0, lambda x,y: (x,y+1), look) or lookDir(0, m, lambda x,y: (x+1,y), look)
            if win: break

        if not win:
           win = lookDir(0, 0, lambda x,y:(x+1,y+1), look) or lookDir(0, 3, lambda x,y:(x+1,y-1), look)

        return win

    winner = None
    if checkWin('X'): winner = 'X'
    elif checkWin('O'): winner = 'O'

    if winner:
        print('Case #{}: {} won'.format(i+1, winner))
    else:
        seenDot = False
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == '.': seenDot = True; break;

        msg = 'Game has not completed' if seenDot else 'Draw'
        print('Case #{}: {}'.format(i+1, msg))
