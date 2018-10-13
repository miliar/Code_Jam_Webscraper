import sys

def main(stream=sys.stdin):
    """
    Input, output, and parsing, etc. Yeah.
    """
    num_cases = int(stream.readline().strip())
    for i in xrange(num_cases):
        rows, cols = map(int, stream.readline().strip().split())
        board = []
        for r in xrange(rows):
            board = board + [map(int, stream.readline().strip().split())]
        if is_board_valid(board, rows, cols):
            print "Case #%d: YES" % (i+1,)
        else:
            print "Case #%d: NO" % (i+1,)

def is_board_valid(board, rows, cols):
    """
    >>> is_board_valid([[1,2,1]], 1, 3)
    True
    """
    return all(all(is_cell_valid(board, r, c) for c in xrange(cols)) for r in xrange(rows))

def is_cell_valid(board, r, c):
    """
    >>> is_cell_valid([ [2, 2, 2, 2, 2], [2, 1, 1, 1, 2], [2, 1, 2, 1, 2], [2, 1, 1, 1, 2], [2, 2, 2, 2, 2] ], 0, 0)
    True
    >>> is_cell_valid([ [2, 2, 2, 2, 2], [2, 1, 1, 1, 2], [2, 1, 2, 1, 2], [2, 1, 1, 1, 2], [2, 2, 2, 2, 2] ], 1, 1)
    False
    """
    return is_cell_row_valid(board, r, c) or is_cell_col_valid(board, r, c)

def is_cell_row_valid(board, r, c):
    """
    >>> is_cell_row_valid([[2,1,2],[1,1,1],[2,1,2]], 1, 1)
    True
    >>> is_cell_row_valid([[2,1,2],[1,1,1],[2,1,2]], 0, 1)
    False
    """
    return all(board[r][i] <= board[r][c] for i in xrange(len(board[r])))

def is_cell_col_valid(board, r, c):
    """
    >>> is_cell_col_valid([[1,2,1]], 0, 1)
    True
    """
    return all(board[i][c] <= board[r][c] for i in xrange(len(board)))

if __name__ == '__main__':
    import doctest
    if doctest.testmod():
        main()
