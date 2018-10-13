infile = open("A-large.in", "rU")
outfile = open("Alarge.out", "w")

def check(row):
    global casenum
    
    if "." in row:
        return False

    elif "X" in row and "O" in row:
        return False

    elif "X" in row:
        outfile.write("Case #%s: X won\n" % casenum)
        return True

    elif "O" in row:
        outfile.write("Case #%s: O won\n" % casenum)
        return True
        
def check_board(board):
    global casenum
    
    # Check rows
    for rownum in xrange(4):
        row = board[rownum]

        if check(row):
            return

    # Check columns
    for colnum in xrange(4):
        column = []

        for rownum in xrange(4):
            column.append(board[rownum][colnum])

        if check(column):
            return

    # Check diagonals
    diag1 = [board[0][0], board[1][1], board[2][2], board[3][3]]

    if check(diag1):
        return

    diag2 = [board[0][3], board[1][2], board[2][1], board[3][0]]

    if check(diag2):
        return

    for row in xrange(4):
        for col in xrange(4):
            if board[row][col] == ".":
                outfile.write("Case #%s: Game has not completed\n" % casenum)
                return

    outfile.write("Case #%s: Draw\n" % casenum)
    return
        
linenum = 0
board = []
casenum = 1

for line in infile:
    if linenum != 0:
        if line.strip() == "":
            check_board(board)
            board = []
            casenum += 1

        else:
            board.append(list(line.strip()))
            
    linenum += 1

outfile.close()
