def checkBoard(board):
    #check col
    for c in range(4):
        col = [r[c] for r in board]
        result = checkWin(col)
        if result != False:
            return result

    #check row
    for row in board:
        result = checkWin(row)
        if result!=False:
            return result

    #check diag
    diag1 = []
    diag2 = []
    c1 = 0
    c2 = 3
    for r in board:
        diag1.append(r[c1])
        diag2.append(r[c2])
        c1 += 1
        c2 -= 1

    result = checkWin(diag1)
    if result != False:
        return result
    result = checkWin(diag2)
    if result != False:
        return result

    #check draw
    for r in board:
        for c in r:
            if c==".":
                return "Game has not completed"

    return "Draw"


def checkWin(move):
    s = list(set(move))
    if len(s) == 2:
        if "T" in s:
            s.remove("T")
    if len(s) == 1:
        if s[0] != ".":
            return "{0} won".format(s[0])
    return False

infile = "A-small-attempt0.in"
f = open(infile, "r")
f_out = open("output", "w")
num = int(f.readline().strip())

for i in range(num):
    board = []

    #read board
    for x in range(4):
        board.append(list(f.readline().strip()))
    f.readline()
    result = checkBoard(board)
    f_out.write("Case #{0}: {1}\n".format(i+1, result))

f.close()
f_out.close()


