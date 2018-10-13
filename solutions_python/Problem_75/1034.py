from sys import *
           
def solve(_, items):
    non_baseDict = dict()
    opposedDict = dict()
    charList = []
    result = []
    i = 0
    C = int(items[i])
    i += 1
    for j in range(C):
        item = items[i + j]
        non_baseDict[(item[0], item[1])] = item[2]
        non_baseDict[(item[1], item[0])] = item[2]
    i += C

    D = int(items[i])
    i += 1
    for j in range(D):
        item = items[i + j]
        opposedDict[item[0]] = item[1]
        opposedDict[item[1]] = item[0]
    i += D

    N = int(items[i])
    i += 1
    charList = items[i]

    for i in range(N):
        char = charList[i]
        result.append(char)
        if len(result) != 1:
            non_base = non_baseDict.get((result[-1], result[-2]))
            if non_base != None:
                result = result[:-2]
                result.append(non_base)
                char = non_base
            opposed = opposedDict.get(char)
            if opposed != None and opposed in result:
                result = []
    result = ', '.join(result)
    print "Case #%d: [%s]" %(_+1, str(result))
    return
    
cases = int(raw_input())
for _ in xrange(cases):
    items = stdin.readline()[:-1].split(' ')
    solve(_, items)
