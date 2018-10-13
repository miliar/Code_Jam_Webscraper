def main():
    file = open("A-large.in")
    lines = file.read().split()
    file.close()
    number = int(lines[0])
    lines = lines[1:]
    boards = []
    for i in range(number):
        lboard = lines[4*i:4*i+4]
        board = []
        for line in lboard:
            board.append(line)
        boards.append(board)
    file = open("3tlarge.txt", 'w')
    file.write(return_output(number, boards))
    file.close()

# file = open("something.txt")
# for line in file:
# file.write

# n is the number in the beginning, s is an array of an array of arrays
# assuming there are no instances when both players have a win
def return_output(n, s):
    result = ""
    for i in range(n):
        result += "Case #" + str(i + 1) + ": "
        board = s[i]
        possibilities = []
        for j in range(4):
            possibilities.append(board[j])
            column = [board[0][j], board[1][j], board[2][j], board[3][j]]
            possibilities.append(column)
        negadiag = [board[0][0], board[1][1], board[2][2], board[3][3]]
        posidiag = [board[3][0], board[2][1], board[1][2], board[0][3]]
        possibilities.append(negadiag)
        possibilities.append(posidiag)
        result += find_win(possibilities)
    return result

def find_win(possibilities):
    complete = True
    for possibility in possibilities:
        # if there is a '.', look in other possibility.
        # if there is are 4Xs or 4Os, with a T, add a win and continue bigger
        # if there are both X and T, look in other possibility.
        if '.' in possibility:
            complete = False
            continue
        elif 'X' in possibility:
            if 'O' in possibility:
                continue
            elif win(possibility):
                return "X won\n"
            continue
        elif win(possibility):
            return "O won\n"
    if complete:
        return "Draw\n"
    else:
        return "Game has not completed\n"


def win(possibility):
    number_t = 0
    for piece in possibility:
        if piece == 'T':
            number_t += 1
    return number_t < 2
