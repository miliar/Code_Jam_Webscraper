pieces = { 'X': 1, 'O':2, 'T':0, '.': 3 }

def create_board(lines):
    x = []
    for line in lines:
        array_line = [pieces[val] for val in line.strip()]
        x.append(array_line)
    return x

def find_winner_horizontal(board):
    missing_pieces = False
    for line in board:
        s = set(line)
        if 3 in s:
            missing_pieces = True
            continue
        if len(s) == 1:
            if 1 in s:
                return 'X', False
            elif 2 in s:
                return 'O', False
        if len(s) == 2 and 0 in s:
            if 1 in s:
                return 'X', False
            elif 2 in s:
                return 'O', False
    return (False, missing_pieces)

def find_winner(board):
    # horizontal search
    result, missing_pieces = find_winner_horizontal(board)
    vert_missing_pieces = False
    diagonal_missing_pieces = False
    if not result:
        # transpose array
        result, vert_missing_pieces = find_winner_horizontal(zip(*board[::-1]))
    if not result:
        diagonal = [[board[0][0], board[1][1], board[2][2], board[3][3]]]
        diagonal.append([board[0][3], board[1][2], board[2][1], board[3][0]])
        result, diagonal_missing_pieces = find_winner_horizontal(diagonal)
    return result, missing_pieces or vert_missing_pieces or diagonal_missing_pieces


def main():
    f = open('test.txt', 'r')
    output = open('output.txt', 'w')
    lines = f.readlines()
    count = int(lines[0])
    line = 1
    board = 1
    while board <= count:
        game_board = create_board(lines[line:line + 4])
        result, missing_pieces = find_winner(game_board)
        if result:
            output.write("Case #%d: %s won\n" % (board, result))
        else:
            if missing_pieces:
                output.write("Case #%d: Game has not completed\n" % board)
            else:
                output.write("Case #%d: Draw\n" % board)
        board = board + 1
        line = line + 5 # line to next board





            
