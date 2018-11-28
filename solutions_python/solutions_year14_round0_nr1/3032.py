import sys


#Opening File
try:
    inputFile = open(sys.argv[1], 'r')
except Exception:
    sys.exit("Could not open file, program terminating")



totalCases = inputFile.readline()


for case in range(1, int(totalCases) + 1):
    firstGuess = inputFile.readline()
    firstGrid = []    
    for i in range(1,5):
        firstGrid.append(set(inputFile.readline().split())) 
    secondGuess = inputFile.readline()
    secondGrid = []
    for i in range(1,5):
        secondGrid.append(set(inputFile.readline().split()))

    gridIntersection = firstGrid[int(firstGuess)-1].intersection(secondGrid[int(secondGuess) - 1])

    if len(gridIntersection) == 0:
        print('Case #' + str(case) + ': Volunteer cheated!')
    elif len(gridIntersection) > 1:
        print('Case #' + str(case) + ': Bad magician!')
    else:
        print('Case #' + str(case) + ': ' + gridIntersection.pop()) 
        
    

