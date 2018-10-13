'''
Created on 07.05.2011

@author: LordB
'''


inFile = open('A-large.in', 'r')
outFile = open('BotTrust_output_large.txt', 'w')

nrOfCases = int( inFile.readline() )

def processLine():
    lineArray = inFile.readline().split()
    for i in range(1, int(lineArray[0])+1 ):
        jobList.append( [lineArray[2*i-1], int(lineArray[2*i])] )

def getBGoalDistance():
    if(len(jobList) == 0): return 0
    for job in jobList:
        if(job[0] == 'B'):
            return abs(bPos - job[1] )
    return 0
   
def getOGoalDistance():
    if(len(jobList) == 0): return 0
    for job in jobList:
        if(job[0] == 'O'):
            return abs(oPos - job[1] )
    return 0     

def disDiff(d1, d2):
    tmp = d1 - d2
    if(tmp < 0):
        return 0
    return tmp

for caseNr in range(1, nrOfCases+1):
    jobList = []
    processLine()
    
    
    oPos = 1
    bPos = 1
    oDist = getOGoalDistance()
    bDist = getBGoalDistance()
    steps = 0

    while(oDist !=0 or bDist !=0 or len(jobList) != 0):
                
        if(jobList[0][0] == 'O'):
            steps += oDist + 1 #press button
            oPos = jobList[0][1]
            bDist = disDiff(bDist, oDist + 1)
            del jobList[0]
            oDist = getOGoalDistance()
        elif(jobList[0][0] == 'B'):
            steps += bDist + 1 #press button
            bPos = jobList[0][1]
            oDist = disDiff(oDist, bDist + 1)
            del jobList[0]
            bDist = getBGoalDistance()

    
    print('Case #{}: {}'.format(caseNr, steps))
    outFile.write('Case #{}: {}\n'.format(caseNr, steps))
    