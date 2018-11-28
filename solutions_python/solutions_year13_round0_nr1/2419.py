class wins():
    X = 'X won'
    O = 'O won'
    CAT = 'Draw'
    NOT_DONE_YET = 'Game has not completed'


def readfile(filename='a.txt'):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    lines.pop(0)

    problems = [''.join(lines[i:i + 4])
                for i in xrange(0, len(lines), 5)]

    return problems


def winning_positions(n=4):
    # horizontal
    for i in xrange(0, n * n, n):
        yield range(i, i + n)

    # vertical
    for i in xrange(n):
        yield range(i, n * n, n)

    # # diagonals (right down)
    yield range(0, n * n, n + 1)

    # # diagonals (left down)
    yield range(n - 1, n * n - 1, n - 1)


def solve(board, positions):
    rows = [[board[i] for i in position]
            for position in positions]

    # skip all with moves
    rows = filter(lambda row: '.' not in row, rows)

    for row in rows:
        r = list(row)
        if 'T' in row:
            r.remove('T')

        if all(map(lambda x: x == 'X', r)):
            return wins.X
        if all(map(lambda x: x == 'O', r)):
            return wins.O

    if '.' in board:
        return wins.NOT_DONE_YET
    else:
        return wins.CAT


positions = list(winning_positions())

with open('out.large.txt', 'wb') as f:
    lines = []
    for i, board in enumerate(readfile('a.large.txt')):
        lines.append('Case #{}: {}\n'.format(i + 1, solve(board, positions)))

    f.writelines(lines)
