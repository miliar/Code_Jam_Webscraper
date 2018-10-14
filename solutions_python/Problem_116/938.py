import sys

def checkHorizontal(board, type, test_no):
    for line in board:
        x = 0
        for c in line:
            if c == 'T' or c == type:
                x += 1

        if x == 4:
            print "Case #" + str(test_no) + ":", type, "won"
            return True

    return False

def checkVertical(board, type, test_no):
    for i in range(4):
        x = 0
        for j in range(4):
            c = board[j][i]
            if c == 'T' or c == type:
                x += 1

        if x == 4:
            print "Case #" + str(test_no) + ":", type, "won"
            return True

    return False

def checkCrossing(board, type, test_no):
    x = 0
    for i,j in zip(range(4), range(4)):
        c = board[j][i]
        if c == 'T' or c == type:
            x += 1

    if x == 4:
        print "Case #" + str(test_no) + ":", type, "won"
        return True

    x = 0
    for i,j in zip(range(4), range(3, -1, -1)):
        c = board[i][j]
        if c == 'T' or c == type:
            x += 1

    if x == 4:
        print "Case #" + str(test_no) + ":", type, "won"
        return True

    return False

number = sys.stdin.readline()
test_cases = int(number)

for test_no in range(1, test_cases + 1):
    count = 0
    board = []

    for i in range(4):
        line = sys.stdin.readline()
        board.append(line)
        for i in range(4):
            c = line[i]
            if c != '.':
                count += 1
    sys.stdin.readline()

    if checkHorizontal(board, 'X', test_no):
        continue
    if checkHorizontal(board, 'O', test_no):
        continue
    if checkVertical(board, 'X', test_no):
        continue
    if checkVertical(board, 'O', test_no):
        continue
    if checkCrossing(board, 'X', test_no):
        continue
    if checkCrossing(board, 'O', test_no):
        continue

    if count == 16:
        print "Case #" + str(test_no) + ": Draw"
    else:
        print "Case #" + str(test_no) + ": Game has not completed"