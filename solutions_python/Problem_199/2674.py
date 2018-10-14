#parameters
allRows = []
allKs = []
inputFileName = 'in.txt'
outputFileName = 'out.txt'

#functions
def readFile():
    with open(inputFileName,'r') as file:
        size = int(file.readline())
        for i in range(size):
            line = file.readline()
            global allRows
            allRows.append(readLine(line))

def readLine(line):
    myList = []
    splitted = line.split()
    global allKs
    allKs.append(int(splitted[1]))
    for c in splitted[0]:
        if c == ' ':
            break
        elif c == '-':
            myList.append(False)
        else:
            myList.append(True)
    return myList

#*** Main ***

#read
readFile()
outputFile = open(outputFileName, 'w+')

print('start')

#loop
for row in range(len(allRows)):
    counter = 0
    k = allKs[row]
    for index in range(len(allRows[row]) - k + 1):
        curr = allRows[row][index]
        if curr == False:
            counter += 1
            for i in range(k):
                allRows[row][index + i] = not allRows[row][index + i]
    if all(allRows[row][-k:]):
        print('Case #{}: {}'.format(row + 1, counter), file = outputFile)
    else:
        print('Case #{}: {}'.format(row + 1, 'IMPOSSIBLE'), file = outputFile)

#close
outputFile.close()


            
        
