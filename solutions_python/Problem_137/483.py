def solver1(R, C, remains):
    for h in xrange(2, R):
        for i in xrange(2, C + 1):
            if i * h == remains:
                return (i, h, 0)
            for j in xrange(2, i + 1):
                if i * h + j == remains:
                    return (i, h, j)
    return None


def stampsquare(board, x, y, w, h):
    for i in xrange(0, w):
        for j in xrange(0, h):
            board[y + j][x + i] = '.'


def solveit():
    R, C, M = [int(x) for x in f.readline().split()]
    solved = True
    transpose = False
    if R > C:
        R, C = C, R
        transpose = True

    remains = R * C - M
    # print R, C, remains
    s1 = solver1(R, C, remains)
    s2 = solver1(R - 1, C, remains - 2)
    s3 = solver1(R - 1, C, remains - 3)
    board = [['*'] * C for i in xrange(0, R)]
    if remains == 1:
        board[0][0] = 'c'
    elif R == 1:
        board[0][0] = 'c'
        for i in xrange(0, remains - 1):
            board[0][i + 1] = '.'
    elif remains == 4:
        stampsquare(board, 0, 0, 2, 2)
        board[0][0] = 'c'
    elif remains == 6:
        stampsquare(board, 0, 0, 3, 2)
        board[0][0] = 'c'
    elif R >= 2 and remains / 2 <= (C + R - 2) and remains % 2 == 0 and remains >= 4:
        if remains / 2 <= C:
            stampsquare(board, 0, 0, remains / 2, 2)
        else:
            stampsquare(board, 0, 0, C, 2)
            stampsquare(board, 0, 0, 2, remains / 2 - C + 2)
        board[0][0] = 'c'
    elif R == 2:
        solved = False
    elif remains == 9:
        stampsquare(board, 0, 0, 3, 3)
        board[0][0] = 'c'
    elif remains == 11:
        stampsquare(board, 0, 0, 3, 3)
        stampsquare(board, 3, 0, 1, 2)
        board[0][0] = 'c'
    elif s1 != None:
        stampsquare(board, 0, 0, s1[0], s1[1])
        stampsquare(board, 0, s1[1], s1[2], 1)
        board[0][0] = 'c'
    elif s2 != None:
        stampsquare(board, 0, 0, s2[0], s2[1])
        stampsquare(board, 0, s2[1], s2[2], 1)
        stampsquare(board, 0, s2[1] + 1, 2, 1)
        board[0][0] = 'c'
    elif s3 != None and s3[2] >= 3:
        stampsquare(board, 0, 0, s3[0], s3[1])
        stampsquare(board, 0, s3[1], s3[2], 1)
        stampsquare(board, 0, s3[1] + 1, 3, 1)
        board[0][0] = 'c'
    else:
        solved = False

    if solved:
        minecount = sum(a == "*" for line in board for a in line)
        scount = sum(a == "c" for line in board for a in line)
        dotcount = sum(a == "." for line in board for a in line)
        assert(minecount == M)
        assert(scount == 1)
        assert(dotcount == R * C - 1 - M)

    output = ""
    if not solved:
        output = "Impossible\n"
    else:
        if not transpose:
            for line in board:
                output += ''.join(line)
                output += "\n"
        else:
            for i in xrange(0, len(board[0])):
                for j in xrange(0, len(board)):
                    output += board[j][i]
                output += "\n"

    if not solved:
        print "not solved", R, C, R * C - M, s1, s2, s3
    return output


outfile = open("results.txt", "w")
with open("test.txt") as f:
    testcases = int(f.readline())

    for i in xrange(0, testcases):
        outcome = solveit()
        # print "Case #%d:" % (i + 1,), outcome
        print >> outfile, "Case #%d:" % (i + 1,)
        outfile.write(outcome)
