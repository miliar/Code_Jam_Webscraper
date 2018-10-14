## google space jam recycled numbers

data = open('/Users/Andrew/Desktop/C-small-attempt0.in', 'r')

numberOfCases = int(data.readline())


def checkIfRecycled( number1, number2 ):
    number1 = str(number1)
    number2 = str(number2)
    matchingPlaces = []

    for index, character in enumerate(number2):
        if (character == number1[0]):
            matchingPlaces.append(index)

    if (len(matchingPlaces) == 0):
        return False

    for matchingPlace in matchingPlaces:
        initialIndex = matchingPlace
        for index in range (0, len(number1)+1):
            if (index == len(number1)):
                return True
            if (number1[index] != number2[ (index + matchingPlace) % len(number1) ]):
                break

    return False


print checkIfRecycled(12, 1212)



for index, line in enumerate(data):
    caseString = line
    case = []
    while True:
        spacePlace = caseString.find(' ')

        if (spacePlace == -1):
            case.append( int(caseString) )
            break

        else:
            case.append(int(caseString[0:spacePlace]))
            caseString = caseString[ (spacePlace +1): ]


    lowerBound = case[0]
    upperBound = case[1]

        
    numberOfRecycled = 0
    for number1 in range(lowerBound, upperBound + 1):
        for number2 in range( lowerBound, number1 ):
            if ( (len(str(number1))==len(str(number2))) and checkIfRecycled( number1, number2 )):
                numberOfRecycled+=1

    print 'Case #%d: %d' %(index+1, numberOfRecycled)


                






        

    
