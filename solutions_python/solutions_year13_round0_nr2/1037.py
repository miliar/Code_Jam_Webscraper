##
# CODEJAM
# prillan91
##
import sys
import re

def solveSingle(f):
    N, M = tuple(int(x) for x in f.readline().strip().split(" "))

    matrix = [[int(x) for x in f.readline().strip().split(" ")] 
              for i in range(N)]

    row_max = range(N)
    col_max = range(M)
    
    for i in range(N):
        row_max[i] = max(matrix[i])
    for j in range(M):
        col_max[j] = max(matrix[i][j] for i in range(N))
            
    for x in range(N):
        for y in range(M):
            if not (matrix[x][y] == row_max[x] or
                    matrix[x][y] == col_max[y]):
                return "NO"

    return "YES"

def solve():
    f = open(sys.argv[1])
    o = open(sys.argv[1] + ".out", 'w')
    T = int(f.readline())

    for t in range(T):
        print t + 1
        o.write("Case #" + str(t + 1) + ": " + str(solveSingle(f)) + "\n")
        

solve()
