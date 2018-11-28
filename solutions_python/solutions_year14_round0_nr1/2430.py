'''
Created on Apr 11, 2014

@author: samirmarin
'''

#import os
#os.chdir('/Users/samirmarin/Documents/UBCSemester2winter20141/cpsc210/JAVAProgram/codeJamQualificationRounds/src/magicTrick')
f_in = open('A-small-attempt1.in', 'r')
f_out = open('A-small-attempt1.out', 'w')

firstLine = f_in.readline().strip()
numCases = int(firstLine)

for i in range(numCases):
    chooseFirstRow = int(f_in.readline().strip())
    for j in range(4):
        rowOne = f_in.readline().strip()
        if j == chooseFirstRow - 1:
            rowOneHold = rowOne
    chooseSecondRow = int(f_in.readline().strip())
    for j in range(4):
        rowTwo = f_in.readline().strip()
        if j == chooseSecondRow - 1:
            rowTwoHold = rowTwo
    
    numListOne = []
    count = 0
    number = ''
    placeInLine = len(rowOneHold)        
    for num in rowOneHold:
        if num != ' ':
            count += 1
            number = number + num
        if num == ' ' or count == placeInLine:
            count += 1
            numListOne = numListOne + [int(number)]
            number = ''
        
    numListTwo = []
    count = 0
    number = ''
    placeInLine = len(rowTwoHold)
    for num in rowTwoHold:
        if num != ' ':
            count += 1
            number = number + num
        if num == ' ' or count == placeInLine:
            count += 1
            numListTwo = numListTwo + [int(number)]
            number = ''
    
    counter = 0   
    for k in range(len(numListOne)):
        for p in range(len(numListTwo)):
            if numListOne[k] == numListTwo[p]:
                counter += 1
                theNum = numListTwo[p]
                
    if counter == 1:
        caseWord = str(theNum)
    elif counter == 0:
        caseWord = 'Volunteer cheated!'
    else:
        caseWord = 'Bad magician!'
        
    f_out.write('Case #' + str(i + 1) + ': ' + caseWord + '\n')
    
f_out.close
            
        
    