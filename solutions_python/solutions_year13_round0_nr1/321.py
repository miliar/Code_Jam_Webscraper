#!/usr/bin/python
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2014
# Tic-Tac-Toe-Tomek
# recherche. Mon idée: utiliser la recherche de chaine dans une autre.

    
def readInts(): return [int(i) for i in raw_input().split()]

def solve(G):
    S = ""
    for i in range(4):
        S += G[i]+"|"
    for j in range(4):
        for i in range(4):
            S += G[i][j]
        S+="|"
    for i in range(4):
        S+=G[i][i]
    S+="|"
    for i in range(4):
        S+=G[3-i][i]

    if S.replace("T","O").find("OOOO")!=-1:
        return "O won"
    if S.replace("T","X").find("XXXX")!=-1:
        return "X won"
    if S.find(".")==-1:
        return "Draw"
    return "Game has not completed"


for test in range(int(raw_input())):
    G = []
    for _  in range(4):
        G.append(raw_input())
    raw_input() # separating empty line
    print 'Case #%d:' % (test+1), solve(G)
