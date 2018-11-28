import sys


if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for n in range(t):
        board = [ list(sys.stdin.readline().strip()) for i in range(4)]
        has_empty = ( len([0 for r in board if '.' in r]) > 0 ) 
        
        for i in range(4):
            x_row = o_row = 0
            x_col = o_col = 0
            x_dia = o_dia = 0
            for j in range(4):
                o_row += 1 if board[i][j] == 'T' or board[i][j] == 'O' else 0
                x_row += 1 if board[i][j] == 'T' or board[i][j] == 'X' else 0
                o_col += 1 if board[j][i] == 'T' or board[j][i] == 'O' else 0
                x_col += 1 if board[j][i] == 'T' or board[j][i] == 'X' else 0
                if i == 0:
                    o_dia += 1 if board[j][j] == 'T' or board[j][j] == 'O' else 0
                    x_dia += 1 if board[j][j] == 'T' or board[j][j] == 'X' else 0
                elif i == 3:
                    o_dia += 1 if board[i-j][j] == 'T' or board[i-j][j] == 'O' else 0
                    x_dia += 1 if board[i-j][j] == 'T' or board[i-j][j] == 'X' else 0
            if o_row == 4 or x_row == 4 or o_col == 4 or x_col == 4 or o_dia == 4 or x_dia == 4:
                break
        else:
            if has_empty:
                print "Case #%d: Game has not completed" %  (n+1)
            else:
                print "Case #%d: Draw" %  (n+1)
            sys.stdin.readline()
            continue
        if o_row == 4 or o_col == 4 or o_dia == 4:
            print "Case #%d: O won" %  (n+1)
        elif x_row == 4 or x_col == 4 or x_dia == 4:
            print "Case #%d: X won" %  (n+1)
        sys.stdin.readline()
        continue
