#!/usr/bin/env python
# -*- coding: utf-8 -*-

X_WON = ['TXXX', 'XTXX', 'XXTX', 'XXXT', 'XXXX']

O_WON = ['TOOO', 'OTOO', 'OOTO', 'OOOT', 'OOOO']

def parse_game():
    def game_generator():
        for _ in xrange(4):
            yield list(raw_input())
    return list(game_generator())


def winning_positions(game):
    # Horizontal
    yield ''.join(game[0])
    yield ''.join(game[1])
    yield ''.join(game[2])
    yield ''.join(game[3])
    # Vertical
    game1 = zip(*game)
    yield ''.join(game1[0])
    yield ''.join(game1[1])
    yield ''.join(game1[2])
    yield ''.join(game1[3])
    # Diagonal
    yield ''.join([game[0][0], game[1][1], game[2][2], game[3][3]])
    yield ''.join([game[3][0], game[2][1], game[1][2], game[0][3]])


def main():
    for i in xrange(input()):
        incomplete = False
        won = None
        for position in winning_positions(parse_game()):
            if position in X_WON:
                won = 'X'
                break
            elif position in O_WON:
                won = 'O'
                break
            elif '.' in position:
                incomplete = True
        if won is not None:
            print 'Case #%d: %s won' % (i + 1, won)
        elif incomplete:
            print 'Case #%d: Game has not completed' % (i + 1)
        else:
            print 'Case #%d: Draw' % (i + 1)
        raw_input()



if __name__ == '__main__':
    main()
