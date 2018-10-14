def check(board):
    """ (4x4 array) -> string
    For given tic-tac-toe board return game state.
    """
    for row in board:
        if row.count("X") == 4 or (row.count("X") == 3 and "T" in row):
            return "X won"
        if row.count("O") == 4 or (row.count("O") == 3 and "T" in row):
            return "O won"

    for i in range(len(board)):
        column = board[0][i] + board[1][i] + board[2][i] + board[3][i]
        if column.count("X") == 4 or (column.count("X") == 3 and "T" in column):
            return "X won"
        if column.count("O") == 4 or (column.count("O") == 3 and "T" in column):
            return "O won"

    diag = board[0][0] + board[1][1] + board[2][2] + board[3][3]
    if diag.count("X") == 4 or (diag.count("X") == 3 and "T" in diag):
            return "X won"
    if diag.count("O") == 4 or (diag.count("O") == 3 and "T" in diag):
        return "O won"

    diag = board[0][3] + board[1][2] + board[2][1] + board[3][0]
    if diag.count("X") == 4 or (diag.count("X") == 3 and "T" in diag):
            return "X won"
    if diag.count("O") == 4 or (diag.count("O") == 3 and "T" in diag):
        return "O won"

    for row in board:
        if "." in row:
            return "Game has not completed"
    return "Draw"

if __name__ == '__main__':
    in_f = open("input.txt", "r")
    out_f = open("output.txt", "w")
    test_cases = int(in_f.readline())
    for case in range(test_cases):
        board = []
        for i in range(4):
            board.append(in_f.readline())
        result = check(board)
        in_f.readline()
        out_f.write("Case #%d: %s\n" % (case+1, result))
    in_f.close()
    out_f.close()
