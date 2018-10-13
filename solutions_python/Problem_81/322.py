'''
Created on 21.05.2011

@author: LordB
'''

inFile = open('A-large.in', 'r')
outFile = open('output_Problem_1_large.txt', 'w')

nrOfCases = int( inFile.readline() )
statistics = []
wr = []
owp = []
oowp = []

def calcWP(i):
    games = 0
    wins = 0
    for c in statistics[i]:
        if (c == '1'):
            wins += 1
            games += 1
        elif(c == '0'):
            games += 1

    wr[i] = ([wins, games])

def calcOWP(i):
    average = 0.0
    games = 0
    counter = 0
    for j in wr:
        if( counter != i):
            if(statistics[i][counter] == '1'):
                average += j[0] / (j[1]-1)
                games += 1
            elif(statistics[i][counter] == '0'):
                average += (j[0]-1) / (j[1]-1)
                games += 1
        counter += 1
    owp[i] = average / games
    
def calcOOWP(i):
    average = 0.0
    nrOfOp = 0
    counter = 0
    for j in owp:
        if(i != counter):
            if(statistics[i][counter] != '.'):
                nrOfOp += 1
                average += j
        counter += 1
    #print('OOWP: ', (average / nrOfOp) )
    oowp[i] = (average / nrOfOp)

for caseNr in range(1, nrOfCases+1):
    print('Working on #', caseNr)
    statistics = []
    wr = []
    owp = []
    oowp = []
    
    nrOfTeams = int( inFile.readline() )
    
    for i in range(nrOfTeams):
        wr.append([])
        owp.append([])
        oowp.append([])
    
    for i in range(nrOfTeams):
        tmp = inFile.readline()
        list = []
        for c in tmp:
            list.append(c)
        statistics.append(list)
    
    for i in range(nrOfTeams):
        calcWP(i)
    for i in range(nrOfTeams):
        calcOWP(i)
    for i in range(nrOfTeams):
        calcOOWP(i)
    
    outFile.write('Case #{}:\n'.format(caseNr))   
    for i in range(nrOfTeams):
        winratio = wr[i][0] / wr[i][1]
        rpi = 0.25 * winratio + 0.5 * owp[i] + 0.25 * oowp[i]
        print(rpi)
        outFile.write( ('{}\n'.format(rpi)) )

    
