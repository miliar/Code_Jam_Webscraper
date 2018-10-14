def check_rows_for_winner(board, player):
    for index in range(0, 13, 4):
        row = board[index:index + 4]
        for c in row:
            if (c != player and c != 'T'):
                break
        else:
            return True
    else:
        return False


def check_columns_for_winner(board, player):
    for index in range(0, 4):
        column = board[index] + board[index + 4] + board[index + 8] + board[index + 12]
        for c in column:
            if (c != player and c != 'T'):
                break
        else:
            return True
    else:
        return False


def check_diagonals_for_winner(board, player):
    left = board[0] + board[5] + board[10] + board[15]
    for c in left:
        if (c != player and c != 'T'):
            break
    else:
        return True
    right = board[3] + board[6] + board[9] + board[12]
    for c in right:
        if (c != player and c != 'T'):
            break
    else:
        return True
    return False


def check_for_winner(board, player):
    if check_rows_for_winner(board, player):
        return True
    elif check_columns_for_winner(board, player):
        return True
    elif check_diagonals_for_winner(board, player):
        return True
    else:
        return False


def check_if_full(board):
    for c in board:
        if (c == '.'):
            return False
    else:
        return True


def read_board(input):
    board = []
    for line in range(4):
        board += list(input.next().strip())
    input.next()
    return board


def analyze_board(board):
    if (check_for_winner(board, 'X')):
        return 'X won'
    elif (check_for_winner(board, 'O')):
        return 'O won'
    elif (check_if_full(board)):
        return 'Draw'
    else:
        return 'Game has not completed'

input = open('A-large.in', 'r')

num_tests = int(input.readline())

for case in range(1, num_tests + 1):
    board = read_board(input)
    outcome = analyze_board(board)
    message = "Case #{case}: {outcome}".format(case=case, outcome=outcome)
    print(message)
