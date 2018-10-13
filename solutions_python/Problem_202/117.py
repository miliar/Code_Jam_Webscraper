def show(i, score, ret):
    print "Case #%s: %s %s" % (i, score, len(ret))
    for x, y, symbol in ret:
        print "%s %s %s" % (symbol, x + 1, y + 1)


def show_board(board):
    print
    print "The board:"
    for row in board:
        print "".join(row)
    print 


def sol_small(board):
    # show_board(board)
    ret = []
    n = len(board)
    other = None
    for y in xrange(n):
        if board[0][y] not in ("+", "."):
            other = (0, y)
            break
    oy = other[1] if other is not None else None

    if other == (0, 0) or other is None:
        if other is None:
            board[0][0] = "o"
            ret.append((0, 0, "o"))
        elif board[0][oy] == "x":
            board[0][oy] = "o"
            ret.append((0, oy, "o"))
        for y in xrange(1, n):
            if board[0][y] == ".":
                board[0][y] = "+"
                ret.append((0, y, "+"))
        for xy in xrange(1, n):
            board[xy][xy] = "x"
            ret.append((xy, xy, "x"))
        for y in xrange(1, n - 1):
            board[n - 1][y] = "+"
            ret.append((n- 1, y, "+"))
    else:
        if board[0][oy] == "x":
            board[0][oy] = "o"
            ret.append((0, oy, "o"))
        for y in xrange(n):
            if board[0][y] == ".":
                board[0][y] = "+"
                ret.append((0, y, "+"))
        cx, cy = 1, oy - 1
        while cy > - 1:
            board[cx][cy] = "x"
            ret.append((cx, cy, "x"))
            cx += 1
            cy -= 1
        cy = oy + 1
        while cx < n:
            board[cx][cy] = "x"
            ret.append((cx, cy, "x"))
            cx += 1
            cy += 1
        for y in xrange(1, n - 1):
            board[n - 1][y] = "+"
            ret.append((n- 1, y, "+"))

    # for x in xrange(n):
    #     for y in xrange(n):
    #         assert check(board, x, y)

    return score(board), ret


def score(board):
    total = 0
    for row in board:
        for el in row:
            if el in ("+", "x"):
                total += 1
            elif el == "o":
                total += 2
    return total


def check(board, x, y):
    n = len(board)

    # Col check
    not_plus = 0
    for i in xrange(n):
        if board[i][y] in ("x", "o"):
            not_plus += 1
            if not_plus > 1:
                return False

    # Row check
    not_plus = 0
    for i in xrange(n):
        if board[x][i] in ("x", "o"):
            not_plus += 1
            if not_plus > 1:
                return False

    # Diag check
    # Main diagonal
    not_x = 0
    cx, cy = x, y
    while cx < n and cy < n:
        if board[cx][cy] in ("+", "o"):
            not_x += 1
            if not_x > 1:
                return False
        cx += 1
        cy += 1
    cx, cy = x - 1, y - 1
    while cx > -1 and cy > -1:
        if board[cx][cy] in ("+", "o"):
            not_x += 1
            if not_x > 1:
                return False
        cx, cy = cx - 1, cy - 1

    # Other diagonal
    not_x = 0
    cx, cy = x, y
    while cx > -1 and cy < n:
        if board[cx][cy] in ("+", "o"):
            not_x += 1
            if not_x > 1:
                return False
        cx, cy = cx - 1, cy + 1
    cx, cy = x + 1, y - 1
    while cx < n and cy > -1:
        if board[cx][cy] in ("+", "o"):
            not_x += 1
            if not_x > 1:
                return False
        cx, cy = cx + 1, cy - 1

    return True


if __name__ == "__main__":
    T = int(raw_input().strip())

    for i in xrange(1, T + 1):
        n, m = map(int, raw_input().strip().split())
        board = [["." for _ in xrange(n)] for _2 in xrange(n)]
        for _ in xrange(m):
            symbol, x, y = raw_input().strip().split()
            x, y = int(x) - 1, int(y) - 1
            board[x][y] = symbol
        show(i, *sol_small(board))

