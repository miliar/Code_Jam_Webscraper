'''
Created on 07.05.2011

@author: LordB
'''

inFile = open('B-large.in', 'r')
outFile = open('output_Magicka.txt', 'w')

nrOfCases = int( inFile.readline() )
#creationRules = []
#destructionRules = []

def extractRule(s):
    list = []
    for c in s:
        list.append(c)
    return list

def getCreationRules(lineArray):
    nrOfRules = int(lineArray[0])
    i = 1
    while(i < nrOfRules+1):
        creationRules.append( extractRule( lineArray[i] ) )
        i += 1

def getDestructionRules(lineArray):
    tmp = int(lineArray[0])
    nrOfRules = int( lineArray[tmp + 1])
    
    i = tmp + 2
    while(i < tmp + 2 + nrOfRules):
        destructionRules.append( extractRule( lineArray[i] ) )
        i += 1
        
def parseInput():
    output = []
    
    for c in lineArray[-1]:
        ruleApplied = False
        
        if(len(output) == 0):
            output.append(c)
        else:
            for rule in creationRules:
                if( (output[-1] == rule[0] and c == rule[1]) or (output[-1] == rule[1] and c == rule[0])):
                    output.pop()
                    output.append(rule[2])
                    ruleApplied = True
                    #print('created ', rule[2])
                    break
            if(ruleApplied == False):
                for rule in destructionRules:
                    for oc in output:
                        if( (c == rule[0] and oc == rule[1]) or (c == rule[1] and oc == rule[0]) ):
                            output = []
                            ruleApplied = True
                            #print('cleared output: ',rule[0],' ',rule[1])
                            break
            if(ruleApplied == False):
                output.append(c)
                
        #print('for c ',c,' inProgressOutput: ', output)
    
    #print(output)
    outFile.write( ('Case #{}: {}\n'.format(caseNr, output)).replace('\'', '') )
            

for caseNr in range(1, nrOfCases+1):
    print('case: ',caseNr)
    creationRules = []
    destructionRules = []
    
    lineArray = inFile.readline().split()
    getCreationRules(lineArray)
    getDestructionRules(lineArray)
    #print('Creation:    ', creationRules)
    #print('Destruction: ', destructionRules)
    
    parseInput()
    