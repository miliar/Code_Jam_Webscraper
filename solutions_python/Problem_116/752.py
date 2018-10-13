import sys

def row_winner(game):
    for i in range(4):
        row_list = [game[i][0],game[i][1],game[i][2],game[i][3]]
        row_list.sort()
        row = "".join(row_list)
        if row == "XXXX" or row == "TXXX":
            return "X"
        elif row == "OOOO" or row == "OOOT":
            return "O"
    else:
        return "C"

def col_winner(game):
    for i in range(4):
        col_list = [game[0][i],game[1][i],game[2][i],game[3][i]]
        col_list.sort()
        col = "".join(col_list)
        if col == "XXXX" or col == "TXXX":
            return "X"
        elif col == "OOOO" or col == "OOOT":
            return "O"
    else:
        return "C"

def diag_winner(game):
    diag_list = [game[0][0],game[1][1],game[2][2],game[3][3]]
    diag_list.sort()
    diag = "".join(diag_list)
    if diag == "XXXX" or diag == "TXXX":
        return "X"
    elif diag == "OOOO" or diag == "OOOT":
        return "O"
    
    diag_list = [game[3][0],game[2][1],game[1][2],game[0][3]]
    diag_list.sort()
    diag = "".join(diag_list)
    if diag == "XXXX" or diag == "TXXX":
        return "X"
    elif diag == "OOOO" or diag == "OOOT":
        return "O"

    return "C"

def num_moves(game):
    return 16 - "".join(game).count(".")

def find_winner(game):
    winner = row_winner(game)
    if winner == "X" or winner == "O":
        return winner + " won"
    winner = col_winner(game)
    if winner == "X" or winner == "O":
        return winner + " won"
    winner = diag_winner(game)
    if winner == "X" or winner == "O":
        return winner + " won"

    if num_moves(game) != 16:
        return "Game has not completed"
    else:
        return "Draw"

name = "A-large"
f = open(name + ".in", "r")
line_num = 0
case_num = 0
cases = {}

for line in f:
    line_num += 1
    if line_num % 5 == 2:
        case_num += 1
        cases[case_num] = [line.strip()]
    elif line_num % 5 == 3:
        cases[case_num].append(line.strip())
    elif line_num % 5 == 4:
        cases[case_num].append(line.strip())
    elif line_num % 5 == 0:
        cases[case_num].append(line.strip())

f.close()
g = open(name + ".out", "w")

for i in range(1, case_num + 1):
    g.write("Case #" + str(i) + ": " + find_winner(cases[i]))
    if i != case_num:
        g.write("\n")