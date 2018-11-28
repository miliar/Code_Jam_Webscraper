# Google Codejam 
# 2013 Qual: Lawnmower

import os

def main():

    os.chdir('/Users/Shane/Documents/codeJam Qual 2013')

    f = open('B-large.in.txt')
    #f = open('B-small-attempt0.in.txt')
    #f = open('LMtest.py')
    o = open('output.txt','w')

    N = int(f.readline())
    
    for i in range(N):
        # Solve problem
        answer = solveProblem(f)

        # Write output
        o.write("Case #" + str(i+1) + ": " + answer + '\n')

    o.close()
    f.close()


def solveProblem(fHandle):

    dim = fHandle.readline().rstrip('\n')
    dim = dim.split()
    N = int(dim[0])
    M = int(dim[1])

    pattern = []

    # Assemble input
    for i in range(N):
        row = fHandle.readline().rstrip('\n').split()
        row = [int(x) for x in row]
        pattern.append(row)

    # Check for validity
    # If every row is convex, pattern is possible
    # If every column is convex, pattern is possible 

    rowMax = [0,]*N
    colMax = [0,]*M
    
    for i in range(N):
        rowMax[i] = max(pattern[i])

    for j in range(M):
        for i in range(N):
            if pattern[i][j] > colMax[j]:
                colMax[j] = pattern[i][j]
            
        
    for i in range(N):
        for j in range(M):
            if (pattern[i][j] != colMax[j]) and (pattern[i][j] != rowMax[i]):
                return "NO"

    return "YES"
