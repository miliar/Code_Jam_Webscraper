#!/usr/bin/env python

input = open("A-large.in", "r")
input.readline()
boards = {}
no = 1
for line in input:
    if line == "\n":
        no = no + 1
        continue
    line = line[:-1]
    if no not in boards:
        boards[no] = []
    boards[no].append(list(line))

def winner(board):
    flipped = [[],[],[],[]]
    finished = True
    for row in board:
        flipped[0].append(row[0])
        flipped[1].append(row[1])
        flipped[2].append(row[2])
        flipped[3].append(row[3])

        if row.count(".") > 0:
            finished = False

        x = row.count("X") + row.count("T")
        o = row.count("O") + row.count("T")
        if o == 4:
            return "O"
        elif x == 4:
            return "X"

    for row in flipped:
        x = row.count("X") + row.count("T")
        o = row.count("O") + row.count("T")
        if o == 4:
            return "O"
        elif x == 4:
            return "X"

    dia1 = [board[0][0], board[1][1], board[2][2], board[3][3]]
    dia2 = [board[0][3], board[1][2], board[2][1], board[3][0]]

    for row in [dia1, dia2]:
        x = row.count("X") + row.count("T")
        o = row.count("O") + row.count("T")
        if o == 4:
            return "O"
        elif x == 4:
            return "X"
    return finished

for board in boards:
    outcome = winner(boards[board])
    if outcome == True:
        print "Case #" + str(board) + ": Draw"
    elif outcome == False:
        print "Case #" + str(board) + ": Game has not completed"
    else:
        print "Case #" + str(board) + ": " + outcome + " won"
