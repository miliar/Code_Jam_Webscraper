import sys

str_xo = ["Draw", "X won", "O won"]
str_not = "Game has not completed"

board_size = 4

def determine(l):
    # 0: None
    # 1: X wins
    # 2: O wins
    x = l.count('X')
    o = l.count('O')
    t = l.count('T')
    if x + t == board_size:
        return 1
    if o + t == board_size:
        return 2
    return 0

def solve(board):
    res = ""

    # horizontal
    for i in range(board_size):
        d = determine(board[i])
        if d > 0:
            return str_xo[d]

    # vertical
    for i in range(board_size):
        l = []
        for aline in board:
            l.append(aline[i])
        d = determine(l)
        if d > 0:
            return str_xo[d]

    # diagonal
    l = []
    for i in range(board_size):
        l.append(board[i][i])
    d = determine(l)
    if d > 0:
        return str_xo[d]

    l = []
    for i in range(board_size):
        l.append(board[i][board_size - i - 1])
    d = determine(l)
    if d > 0:
        return str_xo[d]

    empty_cnt = sum([l.count('.') for l in board])
    if empty_cnt == 0:
        return str_xo[0]
    else:
        return str_not
    return res

if __name__ == '__main__':
    fout = open("%s.out" % (sys.argv[0]), "w")
    num = int(sys.stdin.readline())
    for i in range(num):
        board = []
        while True:
            line = str(sys.stdin.readline()).strip()
            if line == '': break
            board.append(line)
        #print board
        res = solve(board)
        #print res
        fout.write("Case #%d: %s\n" % (i + 1, res))
    fout.close()