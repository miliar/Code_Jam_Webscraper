import sys


OUTCOMES = {
    'X': "X won",
    'O': "O won",
    'D': "Draw",
    'I': "Game has not completed",
}

WIN_POSITIONS_LIST = []

# Add horizontal and vertical wins.
for i in range(4):
    WIN_POSITIONS_LIST.append([[i, j] for j in range(4)])
    WIN_POSITIONS_LIST.append([[j, i] for j in range(4)])

# Add diagonal wins.
WIN_POSITIONS_LIST.append([[i, i] for i in range(4)])
WIN_POSITIONS_LIST.append([[i, 3 - i] for i in range(4)])


def parse_row(row_str):
    result = list(row_str)
    return result

def match(positions, player):
    for pos in positions:
        if pos != player and pos != 'T':
            return False
    return True

def winner(positions):
    for player in ['X', 'O']:
        if match(positions, player):
            return player
    return False

if __name__ == '__main__':
    TESTS = int(sys.stdin.readline())
    for z in range(1, TESTS + 1):
        moves_left = False
        # Read in the game board
        rows = []
        for i in range(4):
            rows.append(parse_row(sys.stdin.readline().strip('\n')))
            if '.' in rows[-1]:
                moves_left = True
        # Identify wins.
        o = False
        for position_indices in WIN_POSITIONS_LIST:
            positions = [rows[i][j] for i, j in position_indices]
            o = winner(positions)
            if o:
                break
        if not o:
            if moves_left:
                o = 'I'
            else:
                o = 'D'
        print("Case #%d: %s" % (z, OUTCOMES[o]))
        # Discard the next line.
        sys.stdin.readline()
