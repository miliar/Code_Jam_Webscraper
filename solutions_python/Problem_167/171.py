def allPossibleValues(V, Dlist):
    D = len(Dlist)
    values = set()
    for k in range(1, 2**D):
        v = 0
        for i in range(D):
            if k & 1<<i != 0:
                v += Dlist[i]
##                print(Dlist[i], end=' ')
##        print('=', v)
        if v <= V:
            values.add(v)
    return values

def solve(V, candidateList, maxUse, newD, Dset, lackValues, possibleValues):
    if newD is not None:
        Dset = Dset | {newD}
        newValues = set(v + newD for v in possibleValues if v+newD <= V) | {newD}
        possibleValues = newValues | possibleValues
        lackValues = lackValues - newValues

    if len(lackValues) == 0:
        return 0
    if len(lackValues) == 1 and maxUse >= 1:
        return 1
    if len(lackValues) == 2:
        small = min(lackValues)
        large = max(lackValues)
        if large - small in possibleValues and maxUse >= 1:
            return 1
        elif maxUse >= 2:
            return 2
        else:
            return None
    if maxUse == 0 or len(candidateList) == 0:
        return None
    minUse = 999999999
    for k, newD in enumerate(candidateList):
        use = solve(V, candidateList[k+1:], min(maxUse-1, minUse), newD, Dset, lackValues, possibleValues)
        if use is not None:
            minUse = min(use, minUse)
    return minUse + 1

def solve1(V, Dlist):
    Dset = set(Dlist)
    possibleValues = allPossibleValues(V, Dlist)
    needValues = set(range(1,V+1))
    lackValues = needValues - possibleValues
    candidateList = [d for d in range(1, V+1) if d not in Dset]

    return solve(V, candidateList, 999999, None, Dset, lackValues, possibleValues)
    
fin = open('C-small-attempt1.in')
caseNum = int(fin.readline())
for caseNo in range(caseNum):
    C, D, V = map(int, fin.readline().strip().split())
    Dlist = list(map(int, fin.readline().strip().split()))
    print('Case #%d: %d' % (caseNo+1, solve1(V, Dlist)))
fin.close()
