import sys
from itertools import islice, chain, izip
from collections import Counter

from utils import stripped_lines


def solve(grid):
    """Solve the grid"""
    unfinished = False

    for line in lines_of_four(grid):
        line = ''.join(line)
        winner = winning(line)
        if winner:
            return '{} won'.format(winner)
        elif not unfinished:
            unfinished = '.' in line
    if unfinished:
        return 'Game has not completed'
    else:
        return 'Draw'


def lines_of_four(grid):
    """Return all lines of four within the grid.

    Args:
        Iterable of strings representing a grid.
    Returns:
        Iterable containing a string for each line of four within grid.
    """
    diagonal_a = (row[i]
                  for i, row in enumerate(grid))
    diagonal_b = (row[-(i + 1)]
                  for i, row in enumerate(grid))

    return chain(
        grid,          # Rows
        izip(*grid),   # Columns
        [diagonal_a,   # Diagonals
         diagonal_b]
    )


def winning(line):
    """Return whether line results in a win, and if so for whom.

    Args:
        String representing line in game grid.
    Returns:
        'X' or 'O' if winning position, else None.
    """
    c = Counter(line)

    if c['.'] or (c['X'] and c['O']):
        return None
    else:
        return 'X' if c['X'] else 'O'


def main():
    lines = stripped_lines(sys.stdin)
    numcases = int(lines.next())

    for i in range(numcases):
        grid = list(islice(lines, 4))
        lines.next()

        result = solve(grid)

        print 'Case #%d: %s' % (i + 1, result)

if __name__ == '__main__':
    main()
