# /user/bin/python
__author__ = 'Pilar Gomez Moya'


def parseInput(fileName, listOfInputs):
    #read raw input from the file
    fo = open(fileName, "r+")
    rawInput = fo.readlines()
    #read the first item that will indicate
    #the number of cases and discard it
    numCases = int(rawInput[0])

    #TODO integrity check: assert the length of rawInput is numCases+1
    #Process each line (each case)
    for x in range(1, numCases+1):
        # split the line (array size + array with numbers of people)
        lineSplitted = rawInput[x].split(' ')
        #TODO integrity check: assert the length is 2
        caseLength = int(lineSplitted[0])
        currentCase = lineSplitted[1]
        #here we will store the formatted output
        listNumPeople = []
        for numPeopleArrayIndex in range(0, caseLength+1):
            listNumPeople.append(int(currentCase[numPeopleArrayIndex]))
        listOfInputs.append(listNumPeople)
    fo.close()


myListOfInputs = []
parseInput("input2.txt", myListOfInputs)
outputFile = open("output.txt", "w+")

numInput = 1
for input in myListOfInputs:

    # Process input n
    extraPeopleNeeded = 0
    shynessLevel = 0
    currentAudienceStanding = 0
    for numPeopleWithSameShyness in input:
        if shynessLevel > currentAudienceStanding:
            if numPeopleWithSameShyness !=0:
                extraPeopleNeeded += shynessLevel-currentAudienceStanding
                currentAudienceStanding +=shynessLevel-currentAudienceStanding

        currentAudienceStanding +=numPeopleWithSameShyness
        shynessLevel+=1

    print "Case #%d: %d"%(numInput, extraPeopleNeeded )
    outputFile.write("Case #%d: %d\n"%(numInput, extraPeopleNeeded ))
    numInput += 1
outputFile.close()



