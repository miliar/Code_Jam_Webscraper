#!/usr/bin/env python

def get_cases():
    f = open("A-small-attempt5.in", "r")
    data = f.readlines()
    f.close()

    case = []
    cases = []

    for line in data[1:]:
        if line != '\n':
            case.append(line.strip())
        else:
            cases.append(case)
            case = []
    return cases


def check_draw(case):
    game_completed = True
    for line in case:
        if line.count('.'):
            game_completed = False
    return game_completed

def check_winner(lines):
    scoreboard = []
    for line in lines:
        for player in ('X', 'O'):
            if line.count(player) == 4 or (line.count(player) == 3 and line.count('T') == 1):
                scoreboard.append(player)

    if len(scoreboard) == 1:
        return scoreboard[0] + " won"
    elif len(scoreboard) == 0:
        return ""

def check_rows(case):
    return check_winner(case)


def check_columns(case):
    column = []
    columns = []
    nb_columns = len(case)
    for i in range(nb_columns):
        for row in case:
            column.append(row[i])
        columns.append(column)
        column = []
    
    return check_winner(columns)

def check_diagonals(case):
    diag1 = []
    diag2 = []
    for i,row in enumerate(case):
        diag1.append(row[i])
        diag2.append(row[len(row)-i-1])

    diagonals = [diag1, diag2]
    return check_winner(diagonals)


def check_result(case):
    ret = check_rows(case)
    if ret:
        return ret
    ret = check_columns(case)
    if ret:
        return ret
    ret = check_diagonals(case)
    if ret:
        return ret
    if check_draw(case):
        return "Draw"
    return "Game has not completed"


fout = open("A-small-attempt5.out", "w")

cases = get_cases()

for i,case in enumerate(cases):
    fout.write("Case #%d: %s\n" % (i+1, check_result(case)))

fout.close()
