'''
Created on May 7, 2011

@author: diego
'''

def decrement(presentElements, element):
    if presentElements[element] == 1:
        del presentElements[element]
    else:
        presentElements[element] = presentElements[element] - 1

def increment(presentElements, element):
    if presentElements.has_key(element):
         presentElements[element] = presentElements[element] + 1
    else:
         presentElements[element] = 1
    
        

def processSpell(combineMap, opposeMap, spell):
    #output
    elementList = []
    #present elements for quick opposite check
    presentElements = dict()
    
    for element in spell:
        combined = False
        cleared = False
        first = False
        if(len(elementList)) == 0:
            elementList.append(element)
            presentElements[element] = 1
            first=True
        else:
            #check for combine
            combineKey = elementList[-1] + element
            if combineMap.has_key(combineKey):
                combined = True
                #modify presentElements
                decrement(presentElements, elementList[-1])                
                elementList[-1] = combineMap[combineKey]
                increment(presentElements, combineMap[combineKey])
                
                
            if combined == False:
                if opposeMap.has_key(element):
                    opponent=opposeMap[element]
                    if presentElements.has_key(opponent):
                        elementList = []
                        presentElements = dict()
                        cleared=True

    
        if(not cleared and not combined and not first):
            elementList.append(element)
            increment(presentElements, element)
        
    return elementList
                      

def parseLine(line):
    line = line.split()
    
    '''combines'''
    combines = int(line[0])
    #like AS combines into T
    combinesMap = dict()
    #like A and T can be combined
#    combinesKeys=dict()
    for i in range(0, combines):
        combine = line[i + 1]
        keys = combine[0:2]
        val = combine[2]
        combinesMap[keys] = val
        combinesMap[keys[::-1]] = val
#        combinesKeys[keys[0]]=keys[1]
#        combinesKeys[keys[1]]=keys[0]
    line = line[combines + 1:]
    '''opposites'''
    opposites = int(line[0])
    oppositesMap = dict()
    
    for i in range(0, opposites):
        opposite = line[i + 1]
        oppositesMap[opposite[0]] = opposite[1]
        oppositesMap[opposite[1]] = opposite[0]
    
    
    line = line[1 + opposites:]
    spell = line[1]
    return (combinesMap, oppositesMap, spell)
    

if __name__ == '__main__':
    file = open('test.dat')
    lines = file.readlines()
    
    lines = lines[1:len(lines)]
    i=1
    for line in lines:
        (combineMap, opposeMap, spell) = parseLine(line)
        output = processSpell(combineMap, opposeMap, spell)
        print 'Case #'+str(i)+': ' + str(output).translate(None, "'")
        i=i+1

