## google code jam google dancing

data = open('/Users/Andrew/Desktop/B-large.in', 'r')

numberOfCases = int(data.readline())

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

    numberOfGoogs = case[0]
    case.pop(0)

    numberOfSurprising = case[0]
    case.pop(0)

    minimumScore = case[0]
    case.pop(0)

    numberOfPossible = 0
    for goog in case:
        if ( (goog - minimumScore >= 0) and (goog - 2*minimumScore+1 >=0) and (goog - 3*minimumScore +2 >=0) ):
            numberOfPossible+=1
        elif ( (numberOfSurprising != 0) and (goog - minimumScore >= 0) and (goog - 2*minimumScore + 2 >= 0) and (goog - 3*minimumScore + 4 >=0)):
            numberOfPossible+=1
            numberOfSurprising-=1

    print 'Case #%d: %d' %(index+1, numberOfPossible)

data.close()
            
            
        
        

    
    
            
            
    
