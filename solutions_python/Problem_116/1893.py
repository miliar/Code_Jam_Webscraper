#!/usr/bin/env python
import sys


def doit(game):
    #print game
    if isDown(game, 'X') or isAcross(game, 'X') or isDiagonal(game, 'X'):
        return 'X won'
    if isDown(game, 'O') or isAcross(game, 'O') or isDiagonal(game, 'O'):
        return 'O won'
    if hasCompleted(game):
        return 'Draw'
    else:
        return 'Game has not completed'


def isDown(game, player):
    for x in range(4):
        won = True
        for y in range(4):
            if game[x][y] != player and game[x][y] != 'T':
                won = False
        if won:
            return True
    return False


def isAcross(game, player):
    for y in range(4):
        won = True
        for x in range(4):
            if game[x][y] != player and game[x][y] != 'T':
                won = False
        if won:
            return True
    return False


def isDiagonal(game, player):
    won = True
    for i in range(4):
        if game[i][i] != player and game[i][i] != 'T':
            won = False
    if won:
        return True
    won = True
    for i in range(4):
        if game[i][3-i] != player and game[i][3-i] != 'T':
            won = False
    return won


def hasCompleted(game):
    for x in range(4):
        for y in range(4):
            if game[x][y] == '.':
                return False
    return True

if __name__ == '__main__' and True:
    cases = int(sys.stdin.readline())
    for case in xrange(1, cases+1, 1):
        game = []
        for i in range(4):
            game += [sys.stdin.readline().rstrip()]
        sys.stdin.readline()
        print "Case #%d: %s" % (case, doit(game))


if __name__ == '__main__':
    assert doit(['XXXX', '....', '....', '....']) == 'X won'
    assert doit(['OOOO', '....', '....', '....']) == 'O won'
    assert doit(['OOTO', '....', '....', '....']) == 'O won'
    assert doit(['OOXX', 'O...', 'O...', 'O...']) == 'O won'
    assert doit(['X...', 'X...', 'X...', 'X...']) == 'X won'
    assert doit(['X...', '.X..', '..X.', '...X']) == 'X won'
    assert doit(['O...', '.O..', '..O.', '...O']) == 'O won'
    assert doit(['T...', '.X..', '..X.', '...X']) == 'X won'
    assert doit(['T...', '.O..', '..O.', '...O']) == 'O won'
    assert doit(['T...', '.O..', '....', '....']) == 'Game has not completed'
    assert doit(['ZZZZ', 'ZZZZ', 'ZZZZ', 'ZZZZ']) == 'Draw'

if __name__ == '__main__' and False:
    for i in range(1000):
        doit(['XXXX', '....', '....', '....'])
