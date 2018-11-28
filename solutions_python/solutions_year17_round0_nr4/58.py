from __future__ import print_function, division
from fileinput import input

inp = input()
t = int(inp.readline())


def score(board):
    s = 0
    for row in board:
        for cell in row:
            if cell == "x" or cell == "+":
                s += 1
            elif cell == "o":
                s += 2
    return s


def get_diff(start_board, paint_board):
    out = []
    n = len(start_board)
    for r in xrange(n):
        for c in xrange(n):
            s = start_board[r][c]
            p = paint_board[r][c]
            if s == p:
                continue
            if s == ".":
                out.append((p, r+1, c+1))
            else:
                assert p == "o"
                out.append((p, r + 1, c + 1))
    return out

def solve(n, board):
    start_board = [["."] * n for _ in xrange(n)]
    paint_board = [["."] * n for _ in xrange(n)]
    for t, r, c in board:
        start_board[r - 1][c - 1] = t
        paint_board[r - 1][c - 1] = t

    pluss = [p for p in board if p[0] == "+" or p[0] == "o"]
    muls = [p for p in board if p[0] == "x" or p[0] == "o"]

    rows = set()
    cols = set(xrange(1, n + 1))
    for _, r, c in muls:
        rows.add(r)
        cols.remove(c)
    cols = list(sorted(cols, key=lambda x: -x))
    for row in xrange(1, n + 1):
        if row not in rows:
            col = cols.pop()
            if paint_board[row - 1][col - 1] == "+":
                paint_board[row - 1][col - 1] = "o"
            elif paint_board[row - 1][col - 1] == ".":
                paint_board[row - 1][col - 1] = "x"
            else:
                assert False

    diffs = set()
    available_sums = set(xrange(0, (2 * (n - 1)) + 1))
    for _, r, c in pluss:
        diffs.add(c - r)
        available_sums.remove(c + r - 2)  # -2 to convert to zero indexing
    for diff in xrange((n - 1), 0, -1):
        if diff not in diffs:
            for row in xrange(n):
                col = row + diff
                if col < 0 or col >= n:
                    continue
                if col + row in available_sums:
                    available_sums.remove(col + row)
                    if paint_board[row][col] == "x":
                        paint_board[row][col] = "o"
                    elif paint_board[row][col] == ".":
                        paint_board[row][col] = "+"
                    else:
                        assert False
                    break
        if -diff not in diffs:
            diff = -diff
            for row in xrange(n):
                col = row + diff
                if col < 0 or col >= n:
                    continue
                if col + row in available_sums:
                    available_sums.remove(col + row)
                    if paint_board[row][col] == "x":
                        paint_board[row][col] = "o"
                    elif paint_board[row][col] == ".":
                        paint_board[row][col] = "+"
                    else:
                        assert False
                    break

    # zero special case
    if 0 not in diffs:
        for i in xrange(n):
            if 2 * i in available_sums:
                available_sums.remove(2 * i)
                if paint_board[i][i] == "x":
                    paint_board[i][i] = "o"
                elif paint_board[i][i] == ".":
                    paint_board[i][i] = "+"
                else:
                    assert False
                break

    # print(paint_board)
    res = get_diff(start_board, paint_board)
    return score(paint_board), len(res), res
    # [("o", 2, 2), ("+", 2, 1), ("x", 1, 1)]


# TODO check coners

for case in xrange(t):
    n, m = map(int, inp.readline().split())
    board = []
    for _ in xrange(m):
        t, r, c = inp.readline().split()
        r = int(r)
        c = int(c)
        board.append((t, r, c))
    res1, res2, liste = solve(n, board)
    print("Case #{}: {} {}".format(case + 1, res1, res2))
    for l in liste:
        print("{} {} {}".format(l[0], l[1], l[2]))
