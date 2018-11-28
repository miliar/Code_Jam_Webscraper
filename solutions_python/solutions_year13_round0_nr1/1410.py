# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 08:47:41 2013

@author: Ivan Koblik
"""

import sys

if len(sys.argv) <= 1:
    print "Expected input file name"
    exit(0)



def read_cases(from_file):
    rows_per_case = 5
    with open(from_file) as f:
        lines = f.readlines()
    num_samples = int(lines[0])
    result = []
    for i in range(num_samples):
        case = lines[1+i*rows_per_case:(i+1)*rows_per_case]
        case = map(lambda s: s[0:rows_per_case-1], case)
        result.append(case)
    return result

FREE = 0
X = 1
O = 2
T = 3
bit_mapping = {"." : FREE, "X" : X, "O" : O, "T" : T}

def convert_case(case):
    size = len(case)
    result = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = bit_mapping[case[i][j]]
    return result

def is_winner(game, player):
    size = len(game)
    #checking rows
    for i in range(size):
        mask = player
        for j in range(size):
            mask &= game[i][j]
            if mask == 0:
                break
        if mask == player:
            return True
    #checking columns
    for j in range(size):
        mask = player
        for i in range(size):
            mask &= game[i][j]
            if mask == 0:
                break
        if mask == player:
            return True
    
    #checking diagonals    
    mask = player
    for i in range(size):
        mask &= game[i][i]
        if mask == 0:
            break
    if mask == player:
        return True

    mask = player
    for i in range(size):
        mask &= game[size-1-i][i]
        if mask == 0:
            break
    if mask == player:
        return True
    
    return False

def moves_available(game):
    for row in game:
        for v in row:
            if v == FREE:
                return True
    return False
     
games = map(convert_case, read_cases(sys.argv[1]))

for i in range(len(games)):
    game = games[i]
    message = "Case #" + str(i+1) + ": "
    if is_winner(game, X):
        message += "X won"
    elif is_winner(game, O):
        message += "O won"
    elif moves_available(game):
        message += "Game has not completed"
    else:
        message += "Draw"
    print message
