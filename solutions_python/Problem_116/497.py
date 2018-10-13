#!/usr/bin/python
# -*- coding:utf-8 -*-

# My python skills are a little bit rusty...

import sys

xwon = "X won"
owon = "O won"
draw = "Draw"
notcompleted = "Game has not completed"

def output(case, status):
    print "Case #%d: %s" % (case, status),


def rows(game):
    return game.split("\n")

def columns(game):
    return [ [game[i], game[i+5], game[i+10], game[i+15]]
             for i in range(0,4) ]

def diagonals(game):
    row = rows(game)

    return [ [row[0][0], row[1][1], row[2][2], row[3][3]],
             [row[0][3], row[1][2], row[2][1], row[3][0]] ]

def check_line(line):
    player = None
    i = 0

    while i<4:
        if line[i] == ".":
            return None
        elif line[i] == "T":
            pass
        else:
            if not player:
                player = line[i]
            elif player != line[i]:
                return None
        i+=1

    return player + " won"


def check(game):
    if game.find(".") >= 0:
        status = notcompleted
    else:
        status = draw

    lines = [row for row in rows(game)] + \
            [column for column in columns(game)] + \
            [diagonal for diagonal in diagonals(game)]


    for line in lines:
        player = check_line(line)
        if player != None:
            return player

    return status


if __name__ == "__main__":
    if len(sys.argv) < 2:
        inputfile = "test_input.txt"
    else:
        inputfile = sys.argv[1]

    f = open(inputfile, "r")
    num = int(f.readline())
    data = f.read()
    f.close()

    games = data.split("\n\n")

    for i in range(0,num):
        status = check(games[i][:19])
        output(i+1, status)
        if i < (num-1):
            print
