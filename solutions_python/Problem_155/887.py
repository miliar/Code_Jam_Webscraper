def readFile(fileName):
    f = open(fileName)
    operaList = []
    for line in f:
        content = line.split()
        if len(content) == 1:
            print content[0],'test cases are read.'
        else:
            operaList.append(content)
    f.close()
    return operaList

def needFriends(opera):
    Smax = int(opera[0])
    friends = 0
    stands = 0
    for Si in range(Smax+1):
##        print 'Si =',Si
        people = int(opera[1][Si])
        if stands >= Si:
            stands += people
        else:
            friends += (Si - stands)
            stands = Si + people
##        print 'stands =',stands,'friends =',friends
    return friends

def solveIt(operaList):
    output = ''
    for j in range(len(operaList)):
        opera = operaList[j]
        friends = needFriends(opera)
        output +=  'Case #{0}: {1}\n'.format(j+1,friends)
    return output[:-1]

def writeOutput(fileName,output):
    f = open(fileName, 'w')
    f.write(output)

##inputFile = 'test.txt'
##outputFile = 'test_output.txt'

inputFile = 'Ab.txt'
outputFile = 'Ab_output.txt'

operaList = readFile(inputFile)
output = solveIt(operaList)
writeOutput(outputFile, output)

print 'Done!'
