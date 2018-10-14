import os
import sys

BOARD_SIZE = 4
SPACE_MAP = {'O': 2,
            'X': 1,
            'T': -1,
            '.': 0}
WINNER_MAP = {1: "X won",
              -1: "X won",
              16: "O won",
              -8: "O won"}
def checkCorners(board):
    diag_right = board[0] * board[5] * board[10] * board[15]
    winner = WINNER_MAP.get(diag_right)
    if winner:
        return winner
    diag_left = board[3] * board[6] * board[9] * board[12]
    winner = WINNER_MAP.get(diag_left)
    if winner:
        return winner
    return

def checkLines(board):
    for i in range(BOARD_SIZE):
        down = board[i] * board[i + 4] * board[i + 8] * board[i + 12]
        winner = WINNER_MAP.get(down)
        if winner:
            return winner
    for i in range(0, BOARD_SIZE*BOARD_SIZE, 4):
        across = board[i] * board[i + 1] * board[i + 2] * board[i + 3]
        winner = WINNER_MAP.get(across)
        if winner:
            return winner
    return

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <input_file>" % sys.argv[0])
        sys.exit(1)
    fin = open(sys.argv[1], 'r')
    fout = open("output.txt", 'w')
    T = int(fin.readline(), 10)
    for case in range(1, T + 1):
        board = []
        for space in range(BOARD_SIZE):
            line = fin.readline().strip()
            for c in line:
                board.append(SPACE_MAP.get(c))
        
        # Clear line after each board
        fin.readline()
        result = checkCorners(board)
        if result:
            fout.write("Case #%d: %s\n" % (case, result) )
            continue
        result = checkLines(board)
        if result:
            fout.write("Case #%d: %s\n" % (case, result))
            continue
        if 0 in board:
            fout.write("Case #%d: Game has not completed\n" % case)
        else:
            fout.write("Case #%d: Draw\n" % case)
    
    fout.close()
    fin.close()