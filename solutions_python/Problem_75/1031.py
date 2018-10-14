f = open('B-small-attempt0.in','r')
out = open('smalloutput.txt','w')

numlines = int(f.readline())

for i in range(numlines):
    vals = f.readline().split(' ')
    
    numCombined = int(vals[0])
    combineDict = {}
    combineResults = {}
    
    for c in range(numCombined):
        combChars = vals[c+1]
        combineDict[combChars[0]] = combChars[1]
        combineDict[combChars[1]] = combChars[0]
        combineResults[combChars[0]] = combChars[2]
        combineResults[combChars[1]] = combChars[2]
    
    numOpposed = int(vals[numCombined+1])
    opposedDict = {}
    
    for c in range(numOpposed):
        opposedChars = vals[numCombined + c + 2]
        opposedDict[opposedChars[0]] = opposedChars[1]
        opposedDict[opposedChars[1]] = opposedChars[0]
    
    numElements = int(vals[numCombined + numOpposed + 2])
    elementList = vals[numCombined + numOpposed + 3]
    
    currentElements = []
    
    for e in range(numElements):
        element = elementList[e]
        
        if(len(currentElements) != 0 and combineDict.has_key(element) and combineDict[element] == currentElements[len(currentElements)-1]):
            currentElements[len(currentElements)-1] = combineResults[element]
        else:
            currentElements.append(element)
        
        last = currentElements[len(currentElements)-1]
        if(opposedDict.has_key(last) and opposedDict[last] in currentElements):
            currentElements = []
    
    out.write('Case #%d: [' % (i+1))
    for c in range(len(currentElements)):
        out.write('%s' % currentElements[c])
        if(c != len(currentElements)-1):
            out.write(', ')
    out.write(']\n')
    print(currentElements)
    