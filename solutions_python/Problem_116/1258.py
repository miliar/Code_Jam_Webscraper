import sys


def winning_row(row):
    if row.count('X') == 4 or (row.count('X') == 3 and row.count('T') == 1):
        return 'X'
    if row.count('O') == 4 or (row.count('O') == 3 and row.count('T') == 1):
        return 'O'
    return None


def solve(B):
    result = None
    empty_fields = 0

    # horizontal
    for row in B:
        result = winning_row(row)
        empty_fields += row.count('.')
        if result:
            return result

    # vertical
    for i in range(4):
        row = []
        for r in B:
            row.append(r[i])
        result = winning_row(row)
        if result:
            return result

    # X
    rowA = []
    rowB = []
    for i in range(4):
        rowA.append(B[i][i])
        rowB.append(B[3-i][i])

    result = winning_row(rowA)
    if result:
        return result

    result = winning_row(rowB)
    if result:
        return result

    if not empty_fields:
        return 'D'

    return result


def main(filename):
    with open(filename, "r") as f:
        T = int(f.readline().strip())
        for t in xrange(T):
            board = []
            for l in range(4):
                board.append([c for c in f.readline().strip()])
            f.readline()
            result = solve(board)
            txt = ""
            if result in ['X', 'O']:
                txt = "%s won" % result
            elif result == 'D':
                txt = 'Draw'
            else:
                txt = 'Game has not completed'
            print "Case #%d: %s" % (t+1, txt)


if __name__ == "__main__":
    main(sys.argv[1])
