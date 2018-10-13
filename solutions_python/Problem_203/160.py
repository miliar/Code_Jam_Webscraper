infilecode = "ALI"

import sys
#import networkx as nx
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = "".join(mapping[c] for c in infilecode)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')

T = int(input())

for case in range(1,T+1):
    
    R, C = map(int,input().split())
    grid = []
    for j in range(R):
        grid += [list(input())]

    print(grid)

    for i in range(1,R):
        r=grid[i]
        if r == ["?"]*C:
            grid[i] = grid[i-1]

    for i in range(R-1,-1,-1):
        r=grid[i]
        #if r != "?"*C:
        #    ok = 1
        if r == ["?"]*C:
            grid[i] = grid[i+1]
    
    print()
    print(grid)

    for i in range(R):
        for j in range(1,C):
            r=grid[i][j]
            if r == "?":
                grid[i][j] = grid[i][j-1]
        for j in range(C-1,-1,-1):
            r=grid[i][j]
            if r == "?":
                grid[i][j] = grid[i][j+1]

    print()
    print(grid)
    


 




    #answer = N - ok
    print("Case #%d:" % case)
    print("Case #%d:" % case, file = output)

    for r in grid:
        print("".join(r))
        print("".join(r), file = output)
