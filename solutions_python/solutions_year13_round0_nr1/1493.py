import doctest
import sys

def main(stream=sys.stdin):
    num_cases = int(stream.readline())
    for i in xrange(1, num_cases+1): # i is 1-based
        board = []
        for row in xrange(4):
            board = board + [stream.readline().strip()]
        print "Case #%d: %s" % (i, get_result(board))
        # waste newline
        stream.readline()

def get_result(board):
    """
    >>> get_result("OOXX OXXX OX.T O..O".split())
    'O won'
    >>> get_result("XOX. OX.. .... ....".split())
    'Game has not completed'
    """
    if did_player_win(board, "O"):
        return "O won"
    elif did_player_win(board, "X"):
        return "X won"
    elif not is_full(board):
        return "Game has not completed"
    else:
        return "Draw"

def is_full(board):
    """
    >>> is_full("XOXT XXOO OXOX XXOO".split())
    True
    >>> is_full("XO.T XXOO OXOX XXOO".split())
    False
    """
    return not any(any(c == '.' for c in row) for row in board)

def did_player_win(board, player):
    """
    >>> did_player_win(["XXXT", "....", "OO..", "...."], "O")
    False
    >>> did_player_win("OOXX OXXX OX.T O..O".split(), "O")
    True
    >>> did_player_win(["OOOT", "....", "XX..", "...."], "O")
    True
    """
    # board is a 4x4 matrix of chars
    assert len(board) == 4
    assert len(board[0]) == 4
    target = player + "T"

    # check horizontal win
    for row in xrange(4):
        winning = all(c in target for c in board[row])
        if winning:
            return True
    # check vertical win
    for col in xrange(4):
        winning = all(board[row][col] in target for row in xrange(4))
        if winning:
            return True
    # check forward diagonal win
    if all(board[x][x] in target for x in xrange(4)):
        return True
    # check reverse diagonal win
    if all(board[x][3-x] in target for x in xrange(4)):
        return True

    return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod():
        main()
