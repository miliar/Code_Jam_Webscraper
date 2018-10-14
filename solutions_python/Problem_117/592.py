output = open('output.txt','w')

inputFile = open('input.txt','r')
n = int(inputFile.readline())
for i in range(n):
    dims = inputFile.readline().split(" ")
    rows = int(dims[0])
    cols = int(dims[1])
    lawnGrid = []
    transposedGrid = []
    
    for m in range(rows):
            row = inputFile.readline().split(" ")
            x = []
            for j in range(cols):
                x.append(int(row[j]))
            lawnGrid.append(x)

    transposedGrid = [list(w) for w in zip(*lawnGrid)]
    possible = True
    for row in range(rows):
        if (possible):
            maxInRow = max(lawnGrid[row])
            for col in range(cols):
                if (possible):
                    maxInCol = max(transposedGrid[col])
                    if lawnGrid[row][col] != maxInRow and lawnGrid[row][col] != maxInCol:
                        possible = False
                        break
    if (possible == True):
##        output.write('\nCase #'+str(i+1)+': YES')
        print('Case #'+str(i+1)+': YES')
    else:
##        output.write('\nCase #'+str(i+1)+': NO')
        print('Case #'+str(i+1)+': NO')


inputFile.close()
output.close()
