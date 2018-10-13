'''
Created on May 22, 2011

@author: michael
'''
def removeAble(i,j,grid):
    if (j+1 < len(grid[i]) and grid[i][j+1] == '#' and 
    i+1 < len(grid) and grid[i+1][j] == '#' and 
    grid[i+1][j+1] == '#'):
        return True
    else:
        return False
def processCase(grid):
    output = ''
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                if removeAble(i,j,grid):
                    grid[i][j] = '/'
                    grid[i][j+1] = '\\'
                    grid[i+1][j] = '\\'
                    grid[i+1][j+1] = '/'
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                return None
    return grid[:]

def readInput(fname):
    cases = []
    inFile = open(fname,'r')
    
    numOfCases = int(inFile.readline().strip())
    
    i = 0
    while i < numOfCases:
        rows,cols = inFile.readline().strip().split(' ')
        case = []
        for j in range(int(rows)):
            case.append(list(inFile.readline().strip()))
        cases.append(case)
        i += 1
    
    inFile.close()
    return cases
def writeOutput(fname,outputs):
    outFile = open(fname,'w')
    
    for i,output in enumerate(outputs):
        if output is not None:
            newOutput = ''
            for j in range(len(outputs[i])):
                for k in range(len(outputs[i][j])):
                    newOutput += outputs[i][j][k]
                newOutput += '\n'
            output = newOutput[:-1]
        else:
            output = 'Impossible'
        outputStr = 'Case #%i:\n%s\n' % (i+1,output)
        outFile.write(outputStr)
    
    outFile.close()
    return None

cases = readInput('A-large.in')
outputs = []
for case in cases:
    outputs.append(processCase(case))
writeOutput('A-large.out',outputs)