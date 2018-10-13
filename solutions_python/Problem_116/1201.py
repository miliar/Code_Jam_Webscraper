ANY = "T"
X = "X"
O = "O"
EMPTY = "."


def solve(board):

    size = len(board)

    diag1 = ANY
    diag2 = ANY
    cols = [ANY for i in range(size)]
    found_empty = False

    for y, row in enumerate(board):

        row_winner = ANY

        for x, v in enumerate(row):

            if v == ANY:
                continue

            if v == EMPTY:
                found_empty = True
                row_winner = EMPTY
                cols[x] = EMPTY
                if x == y:
                    diag1 = EMPTY
                if x == (size - y - 1):
                    diag2 = EMPTY
                continue

            row_winner = v if row_winner in [v, ANY] else EMPTY
            cols[x] = v if cols[x] in [v, ANY] else EMPTY

            if x == y:
                diag1 = v if diag1 in [v, ANY] else EMPTY

            if x == (size - y - 1):
                diag2 = v if diag2 in [v, ANY] else EMPTY

        if row_winner in [X, O]:
            return row_winner

    for v in cols:
        if v in [X, O]:
            return v

    if diag1 in [X, O]:
        return diag1

    if diag2 in [X, O]:
        return diag2

    if found_empty:
        return EMPTY

    return ANY

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):

        board = [raw_input() for _ in range(4)]
        raw_input()
        result = solve(board)

        if result in [X, O]:
            s = "%s won" % result
        elif result == EMPTY:
            s = "Game has not completed"
        else:
            s = "Draw"

        print "Case #%d: %s" % (i+1, s)
