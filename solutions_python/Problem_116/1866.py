"""
Problem A: Tic-Tac-Tomek

"""

def count_values(board):
    horizontal = {}
    vertical = {}
    diagonal_1 = {}
    diagonal_2 = {}

    game_complete = True

    for r in range(0, len(board)):
        for c in range(0, len(board[r])):
            chr = board[r][c]

            if game_complete and chr == '.':
                game_complete = False

            if r not in horizontal:
                horizontal[r] = {}
            if chr not in horizontal[r]:
                horizontal[r][chr] = 0
            horizontal[r][chr] += 1

            if c not in vertical:
                vertical[c] = {}
            if chr not in vertical[c]:
                vertical[c][chr] = 0
            vertical[c][chr] += 1

            if c == r:
                if chr not in diagonal_1:
                    diagonal_1[chr] = 0
                diagonal_1[chr] += 1

            if c + r == len(board[r]) - 1:
                if chr not in diagonal_2:
                    diagonal_2[chr] = 0
                diagonal_2[chr] += 1

    def is_win(fields, score):
        if 'X' in fields:
            if fields['X'] + (fields['T'] if 'T' in fields else 0) == score:
                return 'X'
        if 'O' in fields:
            if fields['O'] + (fields['T'] if 'T' in fields else 0) == score:
                return 'O'

        return None

    score = len(board)

    for r in horizontal:
        res = is_win(horizontal[r], score)
        if res:
            return res, game_complete

    for c in vertical:
        res = is_win(vertical[c], score)
        if res:
            return res, game_complete

    res = is_win(diagonal_1, score)
    if res:
        return res, game_complete

    res = is_win(diagonal_2, score)
    if res:
        return res, game_complete

    return None, game_complete


# Read in boards
boards = []

file = 'A-large'

with open(file + '.in', 'r') as input:
    with open(file + '.out', 'w') as output:
        boards_num = int(input.readline())

        # 5 lines per board
        for i in range(0, boards_num):
            board = []
            for j in range(0, 4):
                line = input.readline()
                board.append(list(line.strip()))

            assert input.readline().strip() == "" # Blank line
            boards.append(board)

            winner, game_complete = count_values(board)

            if winner:
                result = "%s won" % winner.upper()
            else:
                if game_complete:
                    result = "Draw"
                else:
                    result = "Game has not completed"

            output.write("Case #%d: %s\n" % (i + 1, result))