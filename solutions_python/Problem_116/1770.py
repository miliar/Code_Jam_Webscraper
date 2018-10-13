#!/usr/bin/env python

import sys

def solve(game):
    dots = 0
    for i in xrange(4):
        #check rows
        T = game[i].count("T")
        if game[i].count("X")+T == 4: return "X won"
        if game[i].count("O")+T == 4: return "O won"
       
        #check cols
        col = "".join([row[i] for row in game])
        T = col.count("T")
        if col.count("X")+T == 4: return "X won"
        if col.count("O")+T == 4: return "O won"
        
        dots += col.count(".")
   
    d1 = game[0][0] + game[1][1] + game[2][2] + game[3][3] 
    d2 = game[0][3] + game[1][2] + game[2][1] + game[3][0] 

    T = game[i].count("T")
    if d1.count("X")+T == 4: return "X won"
    if d1.count("O")+T == 4: return "O won"
    if d2.count("X")+T == 4: return "X won"
    if d2.count("O")+T == 4: return "O won"
    
    if dots == 0: return "Draw"
    else: return "Game has not completed"
    
cases_no = int(sys.stdin.readline())
for case_no in xrange(cases_no):
    game = []
    for i in xrange(4):
      game.append(sys.stdin.readline()[:-1])
    sys.stdin.readline()
    res = solve(game)
    print "Case #%d: %s" % (case_no+1, res)
