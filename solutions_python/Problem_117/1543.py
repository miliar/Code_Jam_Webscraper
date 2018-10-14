def findPossible(lawn):
    POSS = "YES"
    IMPOSS = "NO"
    smallest = 200
    
    transposedLawn = []
    for x in zip(*lawn):
       transposedLawn += [x]
       
    for i in range(len(lawn)):
        rowPossible = True
        colPossible = True
        smallest = min(lawn[i])
        rowTest = max(lawn[i])
        if rowTest != smallest:
            rowPossible = False
        indices = []
        for p in range(len(lawn[i])):
            if lawn[i][p] == smallest:
                column = p
                colTest = max(transposedLawn[column])
                if colTest != smallest:
                    colPossible = False                     
        if rowPossible == False and colPossible == False:
            return IMPOSS

    return POSS
        
FILENAME = "B-small-attempt1"
f = open(FILENAME + '.in', 'r')
N = int(f.readline())
output = []
for i in range(N):
    temp = f.readline().split(' ')
    M = int(temp[0])
    N = int(temp[1])
    lawn = []
    for p in range(M): #rows
        readLine = f.readline().split(' ')
        line = map(lambda x: int(x), readLine)
        lawn += [line]

    output += ["Case #"+str(i+1)+": " + findPossible(lawn)]


f.close()
output = '\n'.join(e for e in output)
f = open(FILENAME + '.out', 'w')
f.write(output)
f.close()

        
