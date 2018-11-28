##def flip_board(s):
##    old_board = s.splitlines()
##    N = len(old_board)
##    tboard = [[0] * N for i in range(N)]
##    for i in range(N):
##        for j in range(N):
##            tboard[j][N-1-i] = old_board[i][j]
##    board = []
##    return board
         
def flip_board(s):
    old_board = s.splitlines()
    N = len(old_board)
    tboard = [[0] * N for i in range(N)]
    tboard = []
    for i in old_board:
        t = i.replace(".", "")[::-1]
        tboard.append(t + "." * (N- len(t)))
    return tboard


def diag_1(b, idx):
    return "".join(b[i][idx+i] for i in range(len(b) - idx))

def diag_2(b, idx):
    return "".join(b[idx+i][i] for i in range(len(b) - idx))

def diag_3(b, idx):
    N = len(b)
    return "".join(b[idx+i][N - 1 - i] for i in range(len(b) - idx))

def diag_4(b, idx):
    N = len(b)
    return "".join(b[N -1 - idx - i][i] for i in range(len(b) - idx))

def who_wins(board, K):
    N = len(board)
    all_boards = list(board)
    all_boards.extend(["".join([board[i][j] for i in range(N)]) for j in range(N)])
    for i in range(N):
        all_boards.append(diag_1(board, i))
        all_boards.append(diag_2(board, i))
        all_boards.append(diag_3(board, i))
        all_boards.append(diag_4(board, i))

    r = "R" * K
    b = "B" * K
    
    rt = any([r in i for i in all_boards])
    bt = any([b in i for i in all_boards])

    if rt and bt:
        return "Both"
    elif rt:
        return "Red"
    elif bt:
        return "Blue"
    else:
        return "Neither"
    
def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    T = int(lines[0])
    cnt = 1
    R = []
    for i in range(T):
        try:
            t = lines[cnt].split()
            N = int(t[0])
            K = int(t[1])
            res = who_wins(flip_board("".join(lines[cnt+1:cnt+1+N])), K)
            R.append("Case #%d: %s" % (i + 1, res))
            cnt += 1 + N
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(R))

