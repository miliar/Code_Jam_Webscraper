__author__ = 'sigito'

def has_won(board, player):
    is_winning_row = lambda c: c == player or c == 'T'
    # check rows
    for row in board:
        for c in row:
            if not is_winning_row(c):
                break
        else:
            return True

    # check columns
    for column_index in range(4):
        for row in board:
            if not is_winning_row(row[column_index]):
                break
        else:
            return True

    # check diagonal
    for row_index in range(4):
        if not is_winning_row(board[row_index][row_index]):
            break
    else:
        return True

    # check back diagonal
    for row_index in range(4):
        if not is_winning_row(board[row_index][3 - row_index]):
            break
    else:
        return True

    return False


def has_dot(board):
    for row in board:
        if '.' in row:
            return True

    return False


def game_status(board):
    if has_won(board, 'X'):
        return 'X won'
    elif has_won(board, 'O'):
        return 'O won'
    elif has_dot(board):
        return 'Game has not completed'
    else:
        return 'Draw'


def solve():
    test_cases = read_int()
    for test_case in range(1, test_cases + 1):
        board = [read_str() for i in range(4)]
        result = game_status(board)
        print_case(test_case, result)

        if test_case != test_cases:
            read_str()


def test():
    assert game_status(['XXXT', '....', 'OO..', '....']) == 'X won'
    assert game_status(['XOXT', 'XXOO', 'OXOX', 'XXOO']) == 'Draw'
    assert game_status(['XOX.', 'OX..', '....', '....']) == 'Game has not completed'
    assert game_status(['OOXX', 'OXXX', 'OX.T', 'O..O']) == 'O won'
    assert game_status(['XXXO', '..O.', '.O..', 'T...']) == 'O won'
    assert game_status(['OXXX', 'XO..', '..O.', '...O']) == 'O won'


def read_int():
    """
    Reads int from input
    """
    return int(input())


def read_str():
    """
    Reads string from input
    """
    return input()


def read_list_of(type_cast, delimiter=' '):
    """
    Reads line from input and by splitting with `delimiter` and accepting `type_cast` on each element
    forms list. Empty split elements omitted.
    Raises ValueError if `type_cast` is not callable.
    """
    if not callable(type_cast):
        raise ValueError("type_cast must be a mapper function from string to needed type")

    return [type_cast(item) for item in input().split(delimiter) if item]


def print_case(case_index, parameter):
    """
    Prints to standard output "Case #`case_index`: `parameter`".
    """
    print("Case #{case_index}: {data}".format(case_index=case_index, data=parameter))


if __name__ == '__main__':
    solve()