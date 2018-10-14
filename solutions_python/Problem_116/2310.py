#!/usr/bin/python

import sys

T = int(sys.stdin.readline())
lines = sys.stdin.readlines()

def print_game(game):
    for line in game:
        print line

def parse_input(game):
    for line in range(4):
        game[line] = game[line].replace('\n', '')
    return game

def is_incomplete(game):
    for line in game:
        if "." in line:
            return True
    return False

def get_column(game, col):
    return [row[col] for row in game]

def get_linewinner(line):
    T = line.count('T')
    if line.count('O')  + T == 4:
        return 'O'
    elif line.count('X') + T == 4:
        return 'X'
    return None

def get_winner(game):
    for line in game:
        res = get_linewinner(line)
        if res != None:
            return res

    for col in zip(*game):
        res = get_linewinner(col)
        if res != None:
            return res

    dia = [None]*4
    for i in range(0,4):
        dia[i] = game[i][i]

    res = get_linewinner(dia)
    if res != None:
        return res

    for i in range(0,4):
        dia[i] = game[i][3-i]

    res = get_linewinner(dia)
    if res != None:
        return res

    return None 

for i in range(T):
    game = parse_input(lines[i*5:i*5+4])
    print("Case #%d:" % (i+1)),
    winner = get_winner(game)
    if winner == None:
        if is_incomplete(game):
            print("Game has not completed")
        else:
            print("Draw")
    else:
        print("%s won" % (winner))

