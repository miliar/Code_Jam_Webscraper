#!/usr/bin/env python

field_size = 4
symbol_to_int = {".": 0, "X": 1, "O": 2, "T": 3}
class Game:
    field = [[0 for j in range(field_size)] for i in range(field_size)]
    def __init__(self, data):
        self.field = [[0 for j in range(field_size)] for i in range(field_size)]
        for i in range(field_size):
            for j in range(field_size):
                self.field[i][j] = symbol_to_int[data[i*field_size+j]]

    def state(self):
        horizonal = [[0 for j in range(field_size)] for i in range(field_size)]
        vertical = [[0 for j in range(field_size)] for i in range(field_size)]
        diagonal = [[0 for j in range(field_size)] for i in range(2)]
        for i in range(field_size):
            for j in range(field_size):
                horizonal[i][j] = self.field[i][j]
                vertical[j][i] = self.field[i][j]
                if i == j:
                    diagonal[0][i] = self.field[i][j]
                if i == (field_size-1) - j:
                    diagonal[1][i] = self.field[i][j]
        for i in range(field_size):
            ret = self.check(horizonal[i])
            if ret == 1:
                return "X won"
            if ret == 2:
                return "O won"
        for i in range(field_size):
            ret = self.check(vertical[i])
            if ret == 1:
                return "X won"
            if ret == 2:
                return "O won"
        for i in range(2):
            ret = self.check(diagonal[i])
            if ret == 1:
                return "X won"
            if ret == 2:
                return "O won"
        
        for i in range(field_size):
            for j in range(field_size):
                if self.field[i][j] == 0:
                    return "Game has not completed"
        return "Draw"

    def check(self, data):
        ret = 3
        for c in data:
            ret = ret & c
        return ret

        

import sys
size = int(input())
games = []
for i in range(size):
    if i > 0:
        sys.stdin.readline()

    data = "";
    for j in range(field_size):
        data = data + sys.stdin.readline().strip()
    games.append(Game(data))

i = 1
for game in games:
    print "Case #" + str(i) + ": " + game.state()
    i = i + 1
