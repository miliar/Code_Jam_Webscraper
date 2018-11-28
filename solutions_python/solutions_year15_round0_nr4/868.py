__author__ = 'matteo'

def solveNum(X, R, C):
    if((R*C) % X != 0):
        return "RICHARD"
    if(X > C):
        return "RICHARD"
    if(X <= 2):
        return "GABRIEL"
    if(X >= 2*R):
        return "RICHARD"
    if(X < 2*R):
        return "GABRIEL"

def solve(a):
    result = []
    for i in a:
        str = i.split(' ')
        X = int(str[0])
        R = min(int(str[1]), int(str[2]))
        C = max(int(str[1]), int(str[2]))
        result.append(solveNum(X,R,C))
    return result

inputFileName = input("nome file:\n")
fileInput = open(inputFileName, mode='r')
n = int(fileInput.readline())
array = []
for i in range(1,n+1):
    line = fileInput.readline()
    array.append(line)
fileInput.close()
solution = solve(array)
outputFileName = inputFileName + 'Out'
fileOutput = open(outputFileName, mode='w')
count = 1
for i in solution:
    fileOutput.write('Case #' + str(count) + ': ' + i + '\n')
    count += 1
fileOutput.close()

