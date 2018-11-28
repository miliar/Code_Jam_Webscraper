import sys

def containsALetter(row):
    for x in row:
        if x!='?':
            return True
    return False

def splerge(row):
    i=0
    while row[i]=='?':
        i+=1
    char = row[i]
    ret = [char]*(i+1)
    for j in range(i+1,len(row)):
        if row[j]!='?':
            char=row[j]
        ret.append(char)
    return ret

fileName = "A-large"
sys.stdin = open(fileName+".in", 'r')
output = open(fileName+".out", 'w')
T = int(input())
for case in range(1,T+1):

    ###################### input data ###############################

    R,C = input().split(" ")
    R,C = int(R),int(C)
    grid = []
    for r in range(R):
        line = input()
        row = []
        for c in line:
            row.append(c)
        grid.append(row)
    print(grid)

    ######################### compute answer ##################################

    newGrid = []
    i=0
    while not containsALetter(grid[i]):
        i+=1
    row = splerge(grid[i])
    for j in range(i+1):
        newGrid.append(row)
    for j in range(i+1,R):
        if containsALetter(grid[j]):
            row = splerge(grid[j])
        newGrid.append(row)

    ######################## create output file ###############################
    print("Case #%d:" % case, file = output)
    for j in range(R):
        s = ""
        for i in range(C):
            s += newGrid[j][i]
        print(s, file = output)
    ###########################################################################
