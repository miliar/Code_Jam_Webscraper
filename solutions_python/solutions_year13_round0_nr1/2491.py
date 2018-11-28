import sys
from pprint import pprint as pp

def is_winner(board, player_character):
    c = player_character
    chince_sum = 0

    # diagonal nw
    chince_sum = 0
    for i in range(4):
        item = board[i][i]
        if item == c or item == 'T':
            chince_sum += 1

    if chince_sum == 4:
        return True

    # diagonal ne
    chince_sum = 0
    for i in range(4):
        item = board[i][i*-1 - 1]
        if item == c or item == 'T':
            chince_sum += 1

    if chince_sum == 4:
        return True

    # rows
    for i in range(4):
        chince_sum = 0
        for j in range(4):
            item = board[i][j]
            if item == c or item == 'T':
                chince_sum += 1

        if chince_sum == 4:
            return True

    # column
    for j in range(4):
        chince_sum = 0
        for i in range(4):
            item = board[i][j]
            if item == c or item == 'T':
                chince_sum += 1

        if chince_sum == 4:
            return True



def is_full(board):
    for row in board:
        for item in row:
            if item == '.':
                return False
    return True

def board_state(board):
    """ Returns the string status expected from problem """

    if is_winner(board, 'X'):
        return "X won"


    if is_winner(board, 'O'):
        return "O won"

    # we know that no one won, check if board is full
    if (is_full(board)):
        return "Draw"

    return "Game has not completed"

def get_boards(input_file):
    boards = []
    with open(input_file) as file:
        number_of_tests = int(file.readline().rstrip('\n'))

        for test_num in range (number_of_tests):
            board = [['.' for _ in range(4)] for _ in range(4)]

            for i in range(4):
                line = file.readline().rstrip('\n')
                for j in range(len(line)):
                    board[i][j] = line[j]

            # Read an extra line for shits and giggles
            file.readline()

            boards.append(board)

    return boards

def main():
    boards = get_boards(sys.argv[1])
    for i in range(len(boards)):
        #pp(board)
        #print is_full(board)
        print("Case #" + str(i+1) + ": " + board_state(boards[i]))

if __name__ == "__main__":
    main()