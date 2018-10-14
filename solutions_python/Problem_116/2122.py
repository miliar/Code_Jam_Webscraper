# 'X won'
# 'O won'
# 'Draw'
# 'Game has not completed'
if __name__ == '__main__':
    import sys
    f = sys.stdin
    T = int(f.readline())
    for tc in range(1, T + 1):
        board = ''
        tomek = -1
        X = 0
        Y = 0
        for i in range(4):
            ligne = f.readline().rstrip('\r\n')
            board += ligne
            pos = ligne.find('T')
            if pos != -1:
                tomek = i * 4 + pos
            nX = ligne.count('X')
            if (nX == 4) or (nX == 3 and pos != -1):
                X += 1
            elif (nX == 0):
                nY = ligne.count('O')
                if (nY == 4) or (nY == 3 and pos != -1):
                    Y += 1
        # print 'BOARD: ', board
        f.readline() # empty                    
        has_empty = board.find('.') != -1
        final = ''


        if Y == 0 or X == 0:
            # colonne
            for r in range(4):
                c = [board[r], board[r + 4], board[r + 8], board[r + 12]]
                nX = c.count('X')
                pos = -1
                if tomek in [r, r + 4, r + 8, r + 12]:
                    pos = 0
                if (nX == 4) or (nX == 3 and pos != -1):
                    X += 1
                nY = c.count('O')
                if (nY == 4) or (nY == 3 and pos != -1):
                    Y += 1
                if Y == 0 or X == 0:
                    # diagonale 1
                    diag1 = [board[0], board[5], board[10], board[15]]
                    pos = -1
                    if tomek in [0, 5, 10, 15]:
                        pos = 0 # just != -1
                    nX = diag1.count('X')
                    if (nX == 4) or (nX == 3 and pos != -1):
                        X += 1
                    nY = diag1.count('O')
                    if (nY == 4) or (nY == 3 and pos != -1):
                        Y += 1
                    else:
                        # diagonale 2
                        diag2 = [board[3], board[6], board[9], board[12]]
                        pos = -1
                        if tomek in [3, 6, 9, 12]:
                            pos = 0
                        nX = diag2.count('X')
                        if (nX == 4) or (nX == 3 and pos != -1):
                            X += 1
                        nY = diag2.count('O')
                        if (nY == 4) or (nY == 3 and pos != -1):
                            Y += 1            
            if X != 0:
                if Y != 0:
                    final = 'Draw'
                else:
                    final = 'X won'
            elif Y != 0:
                final = 'O won'
            else:
                if has_empty is True:
                    final = 'Game has not completed'
                else:
                    final = 'Draw'
        print 'Case #{nc}: {fnl}'.format(nc=tc, fnl=final)
