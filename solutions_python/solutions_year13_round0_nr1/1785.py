import sys
from itertools import takewhile, imap, islice, repeat

def solve(board):
    columns = zip(*board)
    diagonals = [[row[index] for row, index in zip(board, indexes)] for indexes
                in (range(4), range(3, -1, -1))]
    result = set()
    for line in board + columns + diagonals:
        l = ''.join(sorted(line)).upper()
        if l in {'OOOT', 'OOOO'}:
            result.add('O won')
        elif l in {'TXXX', 'XXXX'}:
            result.add('X won')
    if not result:
        if '.' in ''.join(''.join(row) for row in board):
            result.add('Game has not completed')
        else:
            result.add('Draw')
    if len(result) > 1: result = ['Draw']
    return list(result)[0]


def grouper(l, n):
    return takewhile(lambda x: x,
                     imap(lambda item: list(islice(item, n)),
                          repeat(iter(l))))

if __name__ == '__main__':
    lines = []
    with open(sys.argv[1]) as in_:
        cases = int(next(in_).strip())
        for line in in_:
            if not line.strip():
                continue
            lines.append(line.strip())
    with open(sys.argv[2], 'w') as out:
        for i, board in enumerate(grouper(lines, 4), 1):
            out.write('Case #{}: {}\n'.format(i, solve(board)))
