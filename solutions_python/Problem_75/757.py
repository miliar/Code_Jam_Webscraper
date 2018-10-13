import sys

def addToTrie(x, t):
    letters = [x[0], x[1]]
    letters.sort()
    t[letters[0]] = { letters[1] : x[2]} 
    return t

def searchTrie(x, t):
    letters = [x[0], x[1]]
    if(t.has_key(letters[0])):
        if(t[letters[0]].has_key(letters[1])):
            return t[letters[0]][letters[1]]
    return None

def addToClearList(x, l):
    l.append(set(x))
    return l

def tryClear(x, l):
    for i in range(len(l)):
        if l[i] <= set(x):
            return []
    return x

def magicka(line):
    combinedDict = {}
    opposedList  = []
    elemList = []

    seq = line.split()
    numCombined = int(seq[0])
    rest = seq[1:]
    for i in range(numCombined):
        combinedDict = addToTrie(rest[i], combinedDict)

    numOpposed = int(rest[numCombined])
    rest = rest[numCombined + 1:]
    for i in range(numOpposed):
        opposedList = addToClearList(rest[i], opposedList)
    
    numInvoked = int(rest[numOpposed])
    rest = rest[numOpposed + 1:]
    invoked = []
    for i in range(numInvoked):
        invoked.append(rest[0][i])

    for i in range(len(invoked)):
        elemList.append(invoked[i])
        if len(elemList) == 1:
            continue
        size = len(elemList) - 1
        lastTwo = [elemList[size], elemList[size - 1]]
        lastTwo.sort()
        c = searchTrie(lastTwo, combinedDict)
        if c is not None:
            elemList.pop()
            elemList.pop()
            elemList.append(c)
        elemList = tryClear(elemList, opposedList)

    return elemList

filename = sys.argv[1]
f = open(filename, 'r')
testCases = int(f.readline().split()[0])
for i in range(testCases):
    result = magicka(f.readline())
    fmtResult = '['
    for j in range(len(result)):
        fmtResult += str(result[j])
        if j != len(result)-1:
            fmtResult += ', '
    fmtResult += ']'
    print("Case #" + str(i + 1) + ": " + fmtResult)
f.close()
