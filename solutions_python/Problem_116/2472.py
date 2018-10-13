import sys

# Given a 16 char string representing a board, return the corresponding
# string denoting game state.
def check_board(board, case):
    rows = board.split('\n')
    for row in rows:
        if row in x_wins:
            return 'Case #%d: X won' % case
        elif row in o_wins:
            return 'Case #%d: O won' % case

    columns = [''.join([row[i] for row in rows]) for i in range(4)]
    for col in columns:
        if col in x_wins:
            return 'Case #%d: X won' % case
        elif col in o_wins:
            return 'Case #%d: O won' % case

    diag1 = ''.join([rows[i][i] for i in range(4)])
    if diag1 in x_wins:
        return 'Case #%d: X won' % case
    elif diag1 in o_wins:
        return 'Case #%d: O won' % case

    diag2 = ''.join([rows[i][3-i] for i in range(4)])
    if diag2 in x_wins:
        return 'Case #%d: X won' % case
    elif diag2 in o_wins:
        return 'Case #%d: O won' % case

    if '.' in board:
        return 'Case #%d: Game has not completed' % case
    else:
        return 'Case #%d: Draw' % case

# Given an input to the problem, returns a list of T boards.
def parse_input(path):
    with open(path, 'r') as f:
        raw_w_n = f.read()
        raw = raw_w_n[raw_w_n.find('\n')+1:-2]
        boards = raw.split('\n\n')
        return boards

# Savin things
def gen_winning_configs():
    x_wins = ['XXXX']
    o_wins = ['OOOO']
    for i in range(4):
        x_wins.append('X' * i + 'T' + 'X' * (4 - i - 1))
        o_wins.append('O' * i + 'T' + 'O' * (4 - i - 1))
    return x_wins, o_wins

x_wins, o_wins = gen_winning_configs()

if __name__ == "__main__":
    path = sys.argv[1]

    boards = parse_input(path)

    output = []
    for i in range(len(boards)):
        output.append(check_board(boards[i] , i+1))

    for line in output:
        print line
