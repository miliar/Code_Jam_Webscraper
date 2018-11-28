def addToDict(dictInstance, element):
    if dictInstance.has_key(element):
        dictInstance[element] += 1
    else:
        dictInstance[element] = 1
        
def removeFromDict(dictInstance, element):
    try:
        dictInstance[element] -= 1
        if dictInstance[element] == 0:
            del dictInstance[element]
    except KeyError:
        pass
T = input()
for caseID in range(1,T+1):
    inpTokens = raw_input().split()
    curToken = 0
    C = int(inpTokens[curToken])
    curToken += 1
    comb = {}
    for i in range(0,C):
        combStr = inpTokens[curToken]
        key = ''.join(sorted([combStr[0],combStr[1]]))
        comb[ key ] = combStr[2]
        curToken += 1
    D = int(inpTokens[curToken])
    curToken += 1
    oppose = {}
    for i in range(0,D):        
        c1,c2 = inpTokens[curToken][0], inpTokens[curToken][1]
        if oppose.has_key(c1):
            oppose[c1].append(c2)
        else: oppose[c1] = [c2]
        if oppose.has_key(c2):
            oppose[c2].append(c1)
        else: oppose[c2] = [c1]
        curToken += 1
    
    N = int(inpTokens[curToken])
    curToken += 1
    elementSet = {}
    resultList = []
    elementString = inpTokens[curToken]
    for element in elementString:
        if not resultList:
            resultList.append(element)
            addToDict(elementSet,element)         
        else:
            lastElement = resultList[-1]
            try:
                nxtElement = comb[''.join(sorted([lastElement,element]))]
                del resultList[-1]
                removeFromDict(elementSet,lastElement)
                element = nxtElement
            except KeyError:
                pass
            resultList.append(element)
            addToDict(elementSet,element)
            try:
                #print "curElement %c : %s" % (element, oppose[element
                for opposeElement in oppose[element]:
                    if elementSet.has_key(opposeElement):
                        #print "curElement %c oppose : %c" % (element, opposeElement)
                        resultList = []
                        elementSet.clear()
                        break
            except KeyError:
                pass
        #print resultList
    print "Case #%d: [%s]" % (caseID,', '.join(resultList))
