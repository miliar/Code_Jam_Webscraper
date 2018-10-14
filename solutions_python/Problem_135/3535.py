__author__ = 'mac'


OUTPUT_STRING = "Case #{0}: {1}\n"
CHEATED = "Volunteer cheated!"
BAD = "Bad magician!"

def readMatrix(f):
    array = []
    for i in range(0,4):
        array.append([int(x) for x in f.readline().split()])
    return array

def runTestCase(f):
    firstRow = int(f.readline())-1
    firstMatrix = readMatrix(f)
    secondRow = int(f.readline())-1
    secondMatrix = readMatrix(f)
    return list(set(firstMatrix[firstRow]) & set(secondMatrix[secondRow]))

with open('A-small-attempt0.in','r') as f, open("out.txt",'w') as outF:
    numTests = int(f.readline())
    for i in range(0,numTests):
        result = runTestCase(f)
        if len(result) == 0:
            outF.write(OUTPUT_STRING.format(i+1,CHEATED))
        if len(result) == 1:
            outF.write(OUTPUT_STRING.format(i+1,result[0]))
        if len(result) > 1:
            outF.write(OUTPUT_STRING.format(i+1,BAD))

