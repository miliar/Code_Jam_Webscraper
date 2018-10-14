'''
Created on 31 maj 2010

@author: Jens
'''

fileName = 'B-small-attempt0.in'
#fileName = '3test.txt'
f = open(fileName, 'r')
fOut = open(fileName + 'solution','w')

nrOfCases = int(f.readline()[0:-1])

for caseNr in range(1, nrOfCases+1):
    result = ''
    
    nrOfRounds = int(f.readline()[0:-1])
    
    teams = []
    for team in f.readline()[0:-1].split(" "):
        teams.append(int(team))
    
    for x in range(0,nrOfRounds):
        f.readline()
    
    print teams
    
    pay = 0
    
    #go through the rounds and see how many steps that are needed per round:
    for round in range(0, nrOfRounds):
        #get chunksize:
        size = pow(2,round+1)
        
        #getMinMissesPerGame:
        for x in range(len(teams) / size):
            minMisses = round+100 #safe value
            for index in range(x*size, (x+1)*size):
                if(teams[index] < minMisses):
                    minMisses = teams[index]
            
            if(minMisses <= round):
                pay += 1
        
        print size

    result = str(pay)
    
    print 'Case #' +str(caseNr) + ': ' + result 
    fOut.write('Case #' +str(caseNr) + ': ' + result + '\n')

print 'done'