##
# CODEJAM
# prillan91
##
import sys
import re

def solveSingle(f):
    tlines = [f.readline().strip() for i in [1,2,3,4]]


    for line in tlines:
        print line


    tlines.extend([''.join(tlines[i][i] for i in [0,1,2,3]),
                   ''.join(tlines[i][3-i] for i in [0,1,2,3])])
    tlines.extend([''.join(tlines[j][i] for j in range(4))
                   for i in range(4)])

    f.readline()

    re_x_won = re.compile(r"(X|T){4}")
    re_o_won = re.compile(r"(O|T){4}")
    
    empty = False

    for row in tlines:
        if "." in row:
            empty = True
        if re_x_won.match(row) is not None:
            return "X won"
        if re_o_won.match(row) is not None:
            return "O won"
            
    if empty:
        return "Game has not completed"
    else:
        return "Draw"
            

def solve():
    f = open(sys.argv[1])
    o = open(sys.argv[1] + ".out", 'w')
    T = int(f.readline())

    for t in range(T):
        print t + 1
        o.write("Case #" + str(t + 1) + ": " + str(solveSingle(f)) + "\n")
        

solve()
