inputfile = file("A-large.in", "rb")
outputfile = file("A-large.out", "wb")
out_s = "Case #%d: %s"
T = int( inputfile.readline() )
import pprint
def test_rows(board,i):
    global is_not_drawn
    for row in xrange(4):
        x_can_win, y_can_win = True, True
        for col in xrange(4):
            if board[row][col] == 'X':
                y_can_win = False
            elif board[row][col] == 'O':
                x_can_win = False
            elif board[row][col] == '.':
                x_can_win, y_can_win = False, False
                is_not_drawn = True
        if x_can_win:
            print >>outputfile, out_s % (i+1, "X won")
            return True
        if y_can_win:
            print >>outputfile, out_s % (i+1, "O won")
            return True
    return False

def test_cols(board,i):
    global is_not_drawn
    for col in xrange(4):
        x_can_win, y_can_win = True, True
        for row in xrange(4):
            if board[row][col] == 'X':
                y_can_win = False
            elif board[row][col] == 'O':
                x_can_win = False
            elif board[row][col] == '.':
                x_can_win, y_can_win = False, False
                is_not_drawn = True
        if x_can_win:
            print >>outputfile, out_s % (i+1, "X won")
            return True
        if y_can_win:
            print >>outputfile, out_s % (i+1, "O won")
            return True
    return False

def test_main_diag(board,i):
    global is_not_drawn
    x_can_win, y_can_win = True, True
    for x in xrange(4):
        if board[x][x] == 'X':
            y_can_win = False
        elif board[x][x] == 'O':
            x_can_win = False
        elif board[x][x] == '.':
            x_can_win, y_can_win = False, False
            is_not_drawn = True
    if x_can_win:
        print >>outputfile, out_s % (i+1, "X won")
        return True
    if y_can_win:
        print >>outputfile, out_s % (i+1, "O won")
        return True
    return False

def test_sec_diag(board,i):
    global is_not_drawn
    x_can_win, y_can_win = True, True
    for x in xrange(4):
        if board[x][3-x] == 'X':
            y_can_win = False
        elif board[x][3-x] == 'O':
            x_can_win = False
        elif board[x][3-x] == '.':
            x_can_win, y_can_win = False, False
            is_not_drawn = True
    if x_can_win:
        print >>outputfile, out_s % (i+1, "X won")
        return True
    if y_can_win:
        print >>outputfile, out_s % (i+1, "O won")
        return True
    return False

def test_diags(board, i):
    return test_main_diag(board, i) or test_sec_diag(board, i)


for i in xrange(T):
    board = []
    for j in xrange(4):
        board.append( inputfile.readline()[:-1] ) # Snip newline
    junk = inputfile.readline() # Snip separator
    
    is_not_drawn = False

    # Start with rows
    if test_rows(board,i):
        continue
    if test_cols(board,i):
        continue
    if test_diags(board,i):
        continue

    if is_not_drawn:
        print >>outputfile, out_s % (i+1, "Game has not completed")
    else:
        print >>outputfile, out_s % (i+1, "Draw")

