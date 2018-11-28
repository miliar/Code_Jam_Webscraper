#!/usr/bin/env python3

import sys

def strGameToArray(game: str):
    ret = []
    for line in game.split('\n'):
        line = list(line.strip())
        if line != []:
            ret.append(line)
    return ret

def verticalWon(game):
    possibleWonOffsetsX = {0, 1, 2, 3}
    possibleWonOffsetsO = {0, 1, 2, 3}
    for offset in [0, 1, 2, 3]:
        for line in game:
            if line[offset] != "X" and line[offset] != "T":
                possibleWonOffsetsX -= {offset}
            if line[offset] != "O" and line[offset] != "T":
                possibleWonOffsetsO -= {offset}
    if len(possibleWonOffsetsX) > 0:
        return "X"
    elif len(possibleWonOffsetsO) > 0:
        return "O"
    else:
        return None

def horizontalWon(game):
    for line in game:
        if all((x == "T" or x == "O" for x in line)):
            return "O"
        elif all((x == "T" or x == "X" for x in line)):
            return "X"

def diagonalWon(game):
    def checkRegular(character):
        for point in [game[0][0], game[1][1], game[2][2], game[3][3]]:
            if point not in ["T", character]:
                return False
        return True
    def checkInverse(character):
        for point in [game[3][0], game[2][1], game[1][2], game[0][3]]:
            if point not in ["T", character]:
                return False
        return True
    if checkRegular("X") or checkInverse("X"):
        return "X"
    elif checkRegular("O") or checkInverse("O"):
        return "O"
    else:
        return None

def draw(game):
    for line in game:
        if any((x == "." for x in line)):
            return False
    return True

def status(game):
    stat = verticalWon(game)
    if stat is None:
        stat = horizontalWon(game)
        if stat is None:
            stat = diagonalWon(game)
            if stat is None:
                if draw(game):
                    return "Draw"
                else:
                    return "Game has not completed"
    return stat + " won"

case_count = 1
def cprint(msg):
    global case_count
    print("Case #" + str(case_count) + ": " + msg)
    case_count += 1

def main():
    current = ""
    skipfirst = True
    for line in open(sys.argv[1]):
        if skipfirst:
            skipfirst = False
        elif line.strip() == "":
            cprint(status(strGameToArray(current)))
            current = ""
        else:
            current += line

if __name__ == '__main__':
    main()
