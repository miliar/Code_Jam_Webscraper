__author__ = 'asus'


def testWon(mainBoard, c):
    board = [x for x in mainBoard]
    s = c * 4
    for i in range(4):
        for j in range(4):
            if board[i][j] == "T":
                board[i] = board[i][:j] + c + board[i][j + 1:]
    for i in range(4):
        if board[i] == s:
            return True
        if board[0][i] + board[1][i] + board[2][i] + board[3][i] == s:
            return True
    if board[0][0] + board[1][1] + board[2][2] + board[3][3] == s:
        return True
    if board[0][3] + board[1][2] + board[2][1] + board[3][0] == s:
        return True
    return False

def testDraw(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == ".":
                return False
    return True

fin = open("input.txt", 'r')
fout = open("output.txt", 'w')

n = int(fin.readline())
print n

line = fin.readline()
board = []
i = 0
while len(line) != 0:
    i += 1
    while len(line) == 5:
        board.append(line[:-1])
        line = fin.readline()
    if testWon(board, "X"):
        print "Case #" + str(i) + ": X won"
        fout.write("Case #" + str(i) + ": X won\n")
    elif testWon(board, "O"):
        print "Case #" + str(i) + ": O won"
        fout.write("Case #" + str(i) + ": O won\n")
    elif testDraw(board):
        print "Case #" + str(i) + ": Draw"
        fout.write("Case #" + str(i) + ": Draw\n")
    else:
        print "Case #" + str(i) + ": Game has not completed"
        fout.write("Case #" + str(i) + ": Game has not completed\n")
    board = []
    line = fin.readline()

fin.close()
fout.close()