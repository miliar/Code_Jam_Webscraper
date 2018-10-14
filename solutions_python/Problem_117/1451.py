input = open("B-large.in", "r")
output = open("B-large.out", "w")

numCases = int(input.readline())
for caseNum in range(numCases):
    [numRows, numCols] = map(int, input.readline().split())
    lawn = []
    for rowNum in range(numRows):
        lawn.append(map(int, input.readline().split()))
    
    possible = True
    for rowBlock in range(numRows):
        for colBlock in range(numCols):
            for colNum in range(numCols):
                if lawn[rowBlock][colNum] > lawn[rowBlock][colBlock]:
                    for rowNum in range(numRows):
                        if lawn[rowNum][colBlock] > lawn[rowBlock][colBlock]:
                            possible = False
                            break
                    break
            if not possible:
                break
        if not possible:
            break
    
    if possible:
        outputStr = "YES"
    else:
        outputStr = "NO"
    output.write("Case #" + str(caseNum+1) + ": " + outputStr + "\n")

input.close()
output.close()
