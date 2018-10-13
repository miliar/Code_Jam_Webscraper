'''
Created on Apr 12, 2014

@author: samirmarin
'''

#import os
#os.chdir('/Users/samirmarin/Documents/UBCSemester2winter20141/cpsc210/JAVAProgram/codeJamQualificationRounds/src/cookieClickerAlpha')

f_in = open('B-large.in', 'r')
f_out = open('B-large.out', 'w')

firstLine = f_in.readline().strip()
numCases = int(firstLine)

for i in range(numCases):
    line = f_in.readline().strip()
    
    
    realList = []
    placesInLine = len(line)
    realNumber = ''
    count = 0
    for realNum in line:
        if realNum != ' ':
            count += 1 
            realNumber = realNumber + realNum
        if realNum == ' ' or count == placesInLine:
            count += 1
            realList = realList + [float(realNumber)]
            realNumber = ''
            
    rate = 2.0
    searching = True
    timeHolder = 0
    timeOne = realList[0]/rate
    timeTwo = realList[2]/rate
    while searching:
        
        if timeOne < timeTwo:
            rate = rate + realList[1]
            timeTwoNew = realList[2]/rate + timeOne
            if timeTwoNew < timeTwo:
                timeHolder = timeHolder + timeOne
                timeOne = realList[0]/rate
                timeTwo = realList[2]/rate
            else:
                time = timeTwo + timeHolder
                searching = False
                 
        else:
            time = timeTwo + timeHolder
            searching = False
            
    f_out.write('Case #' + str(i + 1) + ': ' + str(time) + '\n')

f_out.close