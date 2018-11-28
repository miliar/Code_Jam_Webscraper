def  checkForMatch(row1, row2):
    matchesFound = 0
    cardNumber = ''
    
    for i in range(4):
        for j in range(4):
            if(row1[i] == row2[j]):
                cardNumber = row1[i]
                matchesFound += 1
    
    if(matchesFound == 0):
        return 'Volunteer cheated!'
    elif(matchesFound == 1):
        return cardNumber
    elif(matchesFound >= 2):
        return 'Bad magician!'

def main():
    f1 = open('A-small-attempt1.in','r')
    f2 = open('A-small-attempt1.out','w')
    testCaseNumber = int(f1.readline())
    
    counter = 0
    while(counter < testCaseNumber):
        firstAnswer = int(f1.readline())
        matrixA = []
        for i in range(4):
            matrixA.append(f1.readline().strip('\n').split(' '))
        
        secondAnswer = int(f1.readline())
        matrixB = []
        for i in range(4):
            matrixB.append(f1.readline().strip('\n').split(' '))
        
        #print(str(firstAnswer) + " ")
        #print(str(matrixA) + " ")
        #print(str(secondAnswer) + " ")
        #print(str(matrixB) + '\n')
        answer = checkForMatch(matrixA[firstAnswer - 1], matrixB[secondAnswer - 1])
        f2.write('Case #' + str(counter + 1) + ': ' + answer + '\n')
        counter += 1
    
    f1.close()
    f2.close()