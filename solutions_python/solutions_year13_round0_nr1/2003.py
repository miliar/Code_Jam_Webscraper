f = open('C:/Users/vtrinh/Downloads/A-large.in', 'r')
o = open('C:/Users/vtrinh/Downloads/A-large.out', 'w')

T = int(f.readline().strip())

def checkWinner(line):
    no = 0
    nx = 0
    nt = 0
    for i in range(0, 4, 1):
        if line[i] == 'T': nt +=1
        elif line[i] == 'X': nx += 1
        elif line[i] == 'O': no += 1
        else:
            return ""
        if nx == 4 or (nx == 3 and nt == 1):
            return "X won"
            break
        elif no == 4 or (no == 3 and nt == 1):
            return "O won"
            break
    return ""

for t in xrange(T):

    # Read board
    board = ""
    for i in xrange(4):
        board += f.readline().strip()

    f.readline()

    # print len(board)
    res = ""

    for i in range(0, 4, 1):
        # Check for horizontal winner
        row = board[i*4:i*4+4]
        res = checkWinner(row)
        if res <> "":
            break
        else:
            # Check for vertical winner
            col = [board[i], board[i+4], board[i+8], board[i+12]]
            res = checkWinner(col)
            if res <> "":
                break

    if res == "":
        # Check for diagonal 1
        d1 = [ board[0], board[4+1], board[8+2], board[12+3] ]
        res = checkWinner(d1)
        if res == "":
            d2 = [ board[3], board[4+2], board[8+1], board[12] ]
            res = checkWinner(d2)

    # Check for draw/incomplete
    if res == "":
        ndot = 0
        for i in range(len(board)):
            if board[i] == '.':
                ndot += 1
                break
        if ndot > 0:
            res = "Game has not completed"
        else:
            res = "Draw"

    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)