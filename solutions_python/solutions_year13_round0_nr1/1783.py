#!/usr/bin/env python
import sys

flagCompleted = True


def count(s):
    d = {}
    d['T'] = 0
    d['X'] = 0
    d['O'] = 0
    d['.'] = 0

    for m in s:
        d[m] = d[m] + 1
    return d


def eval(s):
    global flagCompleted
    d = count(s)
    #print(d)
    if d['.'] != 0:
        flagCompleted = False

    for k in d:
        if k != '.':
            if d[k] == 3 and d['T'] == 1 or d[k] == 4:
                return k
    return None


if len(sys.argv) == 1:
    f = sys.argv[0][:-2] + 'in'
if len(sys.argv) == 2:
    f = sys.argv[1]


lines = open(f, "r").readlines()
lines = [x.strip() for x in lines if x != '']
varN = int(lines[0])

# Take input lines per varN, varN variables in a case
varN = 6

case = 1

"""Starts from second line !!!"""
for i in range(1, len(lines), varN - 1):
    # varN variables here
    board = []
    for j in range(0, 4):
        board.append(lines[i+j])

    #print(board)
    winner = False
    flagCompleted = True

    # rows
    for j in board:
        e = eval(j)
        if e == 'X' or e == 'O':
            winner = True
            ans = e + " won"
            break
    #print()
    #print()

    # collumns
    if winner is not True:
        for c in range(0, 4):
            col = ''
            for i in board:
                col += i[c]
            #print("Collumn[", c, "]: ", col)
            #for j in col:
            e = eval(col)
            if e == 'X' or e == 'O':
                winner = True
                ans = e + " won"
                break

    if winner is not True:
        d1 = ''
        for di, ri in zip(range(0, 4), board):
            d1 += ri[di]
        #print("diaag1: ", d1)
        e = eval(d1)
        if e == 'X' or e == 'O':
            winner = True
            ans = e + " won"

    if winner is not True:
        d2 = ''
        for di, ri in zip(range(3, -1, -1), board):
            d2 += ri[di]
        #print("diaag2: ", d2)
        e = eval(d2)
        if e == 'X' or e == 'O':
            winner = True
            ans = e + " won"

    if winner is not True:
        if flagCompleted is True:
            ans = "Draw"
        else:
            ans = "Game has not completed"

    print("Case #" + str(case) + ': ' + ans)

    case = case + 1
