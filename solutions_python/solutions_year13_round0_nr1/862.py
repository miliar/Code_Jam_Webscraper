#!/usr/bin/python
import os, sys
import math

nan = float('NaN')

class Game:
    def __init__(self):
        self.vals = table= [ [ 0.0 for i in xrange(4) ] for j in xrange(4) ]

    def add_row(self, row, line):
        global nan
        for c in xrange(0, 4):
            v = str(line[c])
            n = 0.0
            if v == 'T':
                n = 0.0
            elif v == 'O':
                n = -1.0
            elif v == 'X':
                n = 1.0
            elif v == '.':
                n = nan
            else:
                print("UNKNOWN VALUE %s" % (v, ))
            self.vals[row][c] = n

    def sum_row(self, row):
        s = 0.0
        for c in xrange(0, 4):
            s += self.vals[row][c]
        return s

    def sum_col(self, col):
        s = 0.0
        for r in xrange(0, 4):
            s += self.vals[r][col]
        return s

    def sum_diag_down(self):
        s = 0.0
        r = 0
        c = 0
        for i in xrange(0, 4):
            #print("Got (%d, %d) = %f" % (r, c, self.vals[r][c], ))
            s += self.vals[r][c]
            r += 1
            c += 1
        return s

    def sum_diag_up(self):
        s = 0.0
        r = 3
        c = 0
        for i in xrange(0, 4):
            #print("Got (%d, %d) = %f" % (r, c, self.vals[r][c], ))
            s += self.vals[r][c]
            r -= 1
            c += 1
        return s

    def check_game(self, test_num):
        res = "Game has not completed"
        num_x_wins = 0
        num_o_wins = 0
        num_invalid = 0
        dd = self.sum_diag_down()
        if not math.isnan(dd):
            if dd >= 3:
                num_x_wins += 1
            elif dd <= -3:
                num_o_wins += 1
        else:
            num_invalid += 1

        for r in xrange(0, 4):
            rr = self.sum_row(r)
            if not math.isnan(rr):
                if rr >= 3:
                    num_x_wins += 1
                elif rr <= -3:
                    num_o_wins += 1
            else:
                num_invalid += 1

        for c in xrange(0, 4):
            rc = self.sum_col(c)
            if not math.isnan(rc):
                if rc >= 3:
                    num_x_wins += 1
                elif rc <= -3:
                    num_o_wins += 1
            else:
                num_invalid += 1

        du = self.sum_diag_up()
        if not math.isnan(du):
            if du >= 3:
                num_x_wins += 1
            elif du <= -3:
                num_o_wins += 1
        else:
            num_invalid += 1

        if num_x_wins > 0 and num_o_wins > 0:
            res = "Draw"
        elif num_x_wins > 0:
            res = "X won"
        elif num_o_wins > 0:
            res = "O won"
        elif num_invalid == 0:
            res = "Draw"
        print("Case #%d: %s" % (test_num, res))


def read_game(f):
    game = Game()
    for r in xrange(0, 4):
        line = f.readline()
        game.add_row(r, line)

    f.readline()
    return game
        
if len(sys.argv) != 2:
    print("Usage: %s <testfile.txt>" % (sys.argv[0], ))
    exit(0)

filename = sys.argv[1]
f = open(filename, 'r')
num_games = int(f.readline())
#print("Number of games = %d" % (num_games, ))
for game_num in xrange(0, num_games):
    game = read_game(f)
    game.check_game(game_num + 1)
