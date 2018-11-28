'''
Created on 13 mars 2013

@author: Steeve
'''

import sys

def checkX(game, player):
    for i in range(4):
        newLine = game[i].replace("T", player)
        if newLine == player * 4:
            return True
    return False

def getCol(i, game):
    out = ""
    for j in range(4):
        out += game[j][i]
    return out

def checkY(game, player):
    for i in range(4):
        newLine = getCol(i, game).replace("T", player)
        if newLine == player * 4:
            return True
    return False

def checkD1(game, player):
    newLine = ""
    for i in range(4):
        newLine += game[i][i]
    newLine = newLine.replace("T", player)
    return newLine == player * 4

def checkD2(game, player):
    newLine = ""
    for i in range(4):
        newLine += game[i][3-i]
    newLine = newLine.replace("T", player)
    return newLine == player * 4

def hasWon(game, player):
    if checkX(game, player):
        return True
    if checkY(game, player):
        return True
    if checkD1(game, player):
        return True
    if checkD2(game, player):
        return True
    return False

def countDots(game):
    dots = 0
    for k in range(4):
        for l in range(4):
            dots += 1 if game[k][l] == "." else 0
    return dots

out_arr = []
filename = sys.argv[1]
with open(filename) as ifi:
    t = int(ifi.readline())
    for i in range(t):
        square = []
        for j in range(4):
            square.append(ifi.readline()[:-1])
        ifi.readline()
        if hasWon(square, "X"):
            answer = "X won"
        elif hasWon(square, "O"):
            answer = "O won"
        elif countDots(square) > 0:
            answer = "Game has not completed"
        else:
            answer = "Draw"
        out_arr.append("Case #" + str(i + 1) + ": " + str(answer) + "\n")
ofilename = filename.split(".")[0] + ".out"
of = open(ofilename, "w")
of.writelines(out_arr)