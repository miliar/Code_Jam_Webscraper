from sys import stdin, stdout
from pprint import pprint


numCases = int(stdin.readline())
for case in range(1, numCases + 1):
    line = stdin.readline().split()
    combos = {}
    numCombos = int(line[0])
    for i in range(1, numCombos + 1):
        triplet = line[i]
        combos[triplet[0] + triplet[1]] = triplet[2]
        combos[triplet[1] + triplet[0]] = triplet[2]
    opps = set()
    numOpp = int(line[numCombos + 1])
    for i in range(numCombos + 2, numCombos + numOpp + 2):
        pair = line[i]
        opps.add(pair) 
        opps.add(pair[1] + pair[0])

    invokeOrder = line[numCombos + numOpp + 3]
    invokeList = []
    for call in invokeOrder:
        clearList = False
        if len(invokeList) > 0:
            last = invokeList.pop()
            if (call + last) in combos:
                invokeList.append(combos[call + last])
                continue
            else:
                invokeList.append(last)
                for check in invokeList:
                    if (check + call) in opps:
                        invokeList = []
                        clearList = True
                        break
            if not clearList:
                invokeList.append(call)
        else:
            invokeList.append(call)

    stdout.write("Case #%s: " % case)
    liststr = str(invokeList)
    liststr = liststr.replace("\'", "")
    print liststr



