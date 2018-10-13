#GCJ2013/1/1
#aaimnr
#Python v3

import sys, os, operator

def lines():
    line_cords =   [(x,y) for x in range(4) for y in range(4)] +  [(y,x) for x in range(4) for y in range(4)]
    diags = [(x,x) for x in range(4)] + [(x,3-x) for x in range(4)]
    coords =  diags + line_cords
    return [coords[n:n+4] for n in range(0, len(coords),4 ) ]

def solve_case(tab):
    dots = 0
    for line in lines:
        (o,x)=(0,0)
        for p in line:
            cell = tab[p[0]][p[1]]
            if cell == ".":
                dots=dots+1
                break
            elif cell == "X":
                x=x+1
            elif cell == "O":
                o=o+1
            elif cell == "T":
                x=x+1
                o=o+1
        if x==4:
            return "X won"
        if o==4:
            return "O won"
    if dots>0:
        return "Game has not completed"
    else:
        return "Draw"

f = sys.stdin
lines = lines()
cases = int(f.readline())
for case in range(1, cases+1):
    tab = []
    for i in range(4):
        tab.append(f.readline())
    f.readline()
    res = solve_case(tab)
    print('Case #%d: %s'%(case, res))































