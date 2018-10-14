__author__ = 'louyang'

# Input

# The first line of the input gives the number of test cases,
# T. T test cases follow. Each test case consists of 4 lines
# with 4 characters each, with each character being 'X', 'O', '.' or 'T'
# (quotes for clarity only). Each test case is followed by an empty line.

# Output

# For each test case, output one line containing "Case #x: y", where x is the case
# number (starting from 1) and y is one of the statuses given above. Make sure to
# get the statuses exactly right. When you run your code on the sample input, it
# should create the sample output exactly, including the "Case #1: ", the capital
# letter "O" rather than the number "0", and so on.

def check_four(four):
    counts = {}
    for c in four:
        if counts.get(c):
            counts[c] += 1
        else:
            counts[c] = 1
    for k, v in counts.items():
        if (k == 'X' or k == 'O') and v >= 3:
            if v == 4:
                return True
            if v == 3:
                if 'T' in counts.keys():
                    return True
    return False


def get_status(board):
    global not_completed
    message = None
    not_completed = False
    for i in range(4):
        def wrap_inner():
            global not_completed
            for j in range(4):
                cur = board[i][j]
                if cur == '.':
                    not_completed = True
                    continue

                if i-2 > -1 and i+1 < 4:
                    four = []
                    four.append(board[i-2][j])
                    four.append(board[i-1][j])
                    four.append(board[i+1][j])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"

                if i-1 > -1 and i+2 < 4:
                    four = []
                    four.append(board[i-1][j])
                    four.append(board[i+1][j])
                    four.append(board[i+2][j])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"

                if j-2 > -1 and j+1 < 4:
                    four = []
                    four.append(board[i][j-2])
                    four.append(board[i][j-1])
                    four.append(board[i][j+1])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"
                if j-1 > -1 and j+2 < 4:
                    four = []
                    four.append(board[i][j-1])
                    four.append(board[i][j+1])
                    four.append(board[i][j+2])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"
                if i-2 > -1 and j-2 > -1 and j+1 < 4 and i+1 < 4:
                    four = []
                    four.append(board[i-2][j-2])
                    four.append(board[i-1][j-1])
                    four.append(board[i+1][j+1])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"
                if i-1 > -1 and j-1 > -1 and j+2 < 4 and i+2 < 4:
                    four = []
                    four.append(board[i-1][j-1])
                    four.append(board[i+1][j+1])
                    four.append(board[i+2][j+2])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"
                if i+2 < 4 and j-2 > -1 and i-1 > -1 and j+1 < 4:
                    four = []
                    four.append(board[i-1][j+1])
                    four.append(board[i+1][j-1])
                    four.append(board[i+2][j-2])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"
                if i+1 < 4 and j-1 > -1 and i-2 > -1 and j+2 < 4:
                    four = []
                    four.append(board[i-1][j+1])
                    four.append(board[i+1][j-1])
                    four.append(board[i-2][j+2])
                    four.append(cur)
                    if check_four(four):
                        return cur + " won"
        msg = wrap_inner()
        if msg:
            message = msg
            break
    if not message:
        if not_completed:
            return "Game has not completed"
        return "Draw"
    not_completed = False
    return message


num_tests = input()
for i in range(num_tests):
    board = []
    for j in range(4):
        board.append(list(raw_input().strip()))
    if i != num_tests - 1:
        raw_input() # consume empty line, unless we are at end
    print "Case #" + str(i + 1) + ":", get_status(board)
