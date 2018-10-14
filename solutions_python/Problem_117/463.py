def isMowable(lawn):
    rowDominators = [[0]*len(lawn[0]) for i in range(len(lawn))]
    colDominators = [[0]*len(lawn[0]) for i in range(len(lawn))]
    
    for i in range(len(lawn)):
        row = lawn[i]
        maxRow = max(row)
        for j in range(len(row)):
            if row[j] == maxRow:
                rowDominators[i][j] = 1

    for i in range(len(lawn[0])):
        col = []
        for j in range(len(lawn)):
            col += [lawn[j][i]]
        maxCol = max(col)
        for j in range(len(col)):
            if col[j] == maxCol:
                colDominators[j][i] = 1

    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            if rowDominators[i][j] == 0 and colDominators[i][j] == 0:
                return "NO"
    return "YES"
    
    '''for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            cellHeight = lawn[i][j]
            vertPossible = True
            horizPossible = True
            for k in range(len(lawn)):
                if lawn[k][j] > cellHeight:
                    vertPossible = False
                    break
            for k in range(len(lawn[i])):
                if lawn[i][k] > cellHeight:
                    horizPossible = False
                    break
            if not vertPossible and not horizPossible:
                return "NO"
    return "YES"'''


filename = "B-large (3).in"
outputname = filename + "out.txt"

inFile = open(filename, 'r')
outFile = open(outputname, 'w')


numTests = int(inFile.readline())

    

for i in range(numTests):
    dimensions = inFile.readline().split()
    n = int(dimensions[0])
    m = int(dimensions[1])
    lawn = []
    for j in range(n):
        line = inFile.readline().split()
        for k in range(m):
            line[k] = int(line[k])
        lawn += [line]

    answer = isMowable(lawn)
    
    
    outFile.write("Case #" + str(i+1) + ": " + answer + '\n')
    print "Case #" + str(i+1) + ": " + answer

inFile.close()
outFile.close()
