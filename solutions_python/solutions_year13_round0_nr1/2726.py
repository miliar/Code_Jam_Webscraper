def main():
    scanner = open('A-small-attempt1.in','r')
    writer = open('A-small-attempt1.out','w')
    T = int(scanner.readline())
    X = 1
    while T > 0:
        board = []
        row = 0
        while row < 4:
            board.append(scanner.readline())
            row += 1
        
        row = 0
        win = ''
        while row < 4:
            if board[row][0] == 'X' or board[row][0] == 'O':
                col = 1
                while col < 4:
                    if board[row][col] != board[row][0] and board[row][col] != 'T':
                        break
                    col += 1
                if col == 4:
                    if board[row][0] == 'X':
                        win = 'X won'
                    else:
                        win = 'O won'
                    break
            elif board[row][0] == 'T':
                if board[row][1] == 'X' or board[row][1] == 'O':
                    col = 2
                    while col < 4:
                        if board[row][col] != board[row][1] and board[row][col] != 'T':
                            break
                        col += 1
                    if col == 4:
                        if board[row][1] == 'X':
                            win = 'X won'
                        else:
                            win = 'O won'
                        break
            row += 1
        if len(win) == 0:
            col = 0
            while col < 4:
                if board[0][col] == 'X' or board[0][col] == 'O':
                    row = 1
                    while row < 4:
                        if board[row][col] != board[0][col] and board[row][col] != 'T':
                            break
                        row += 1
                    if row == 4:
                        if board[0][col] == 'X':
                            win = 'X won'
                        else:
                            win = 'O won'
                        break
                elif board[0][col] == 'T':
                    if board[1][col] == 'X' or board[1][col] == 'O':
                        row = 2
                        while row < 4:
                            if board[row][col] != board[1][col] and board[row][col] != 'T':
                                break
                            row += 1
                        if row == 4:
                            if board[1][col] == 'X':
                                win = 'X won'
                            else:
                                win = 'O won'
                            break
                col += 1
        if len(win) == 0:
            if board[0][0] == 'X' or board[0][0] == 'O':
                diag = 1
                while diag < 4:
                    if board[diag][diag] != board[0][0] and board[diag][diag] != 'T':
                        break
                    diag += 1
                if diag == 4:
                    if board[0][0] == 'X':
                        win = 'X won'
                    else:
                        win = 'O won'
            elif board[0][0] == 'T':
                if board[1][1] == 'X' or board[1][1] == 'O':
                    diag = 2
                    while diag < 4:
                        if board[diag][diag] != board[1][1] and board[diag][diag] != 'T':
                            break
                        diag += 1
                    if diag == 4:
                        if board[1][1] == 'X':
                            win = 'X won'
                        else:
                            win = 'O won'
        if len(win) == 0:
            if board[3][0] == 'X' or board[3][0] == 'O':
                diag = 2
                diag2 = 1
                while diag2 < 4:
                    if board[diag][diag2] != board[0][0] and board[diag][diag2] != 'T':
                        break
                    diag -= 1
                    diag2 += 1
                if diag2 == 4:
                    if board[3][0] == 'X':
                        win = 'X won'
                    else:
                        win = 'O won'
            elif board[3][0] == 'T':
                if board[2][1] == 'X' or board[2][1] == 'O':
                    diag = 1
                    diag2 = 2
                    while diag2 < 4:
                        if board[diag][diag2] != board[2][1] and board[diag][diag2] != 'T':
                            break
                        diag -= 1
                        diag2 += 1
                    if diag2 == 4:
                        if board[2][1] == 'X':
                            win = 'X won'
                        else:
                            win = 'O won'
        if len(win) == 0:
            row = 0
            while row < 4:
                if '.' in board[row]:
                    win = 'Game has not completed'
                    break
                row += 1
        if len(win) == 0:
            win = 'Draw'
        writer.write('Case #%d: %s\n' % (X, win))
        scanner.readline()
        X += 1
        T -= 1

if __name__ == '__main__':
    main()
    