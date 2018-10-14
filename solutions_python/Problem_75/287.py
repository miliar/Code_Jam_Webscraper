
def strSort(a, b):
    if a < b:
        return a + b
    else:
        return b + a

# inlist: list of chars
# oppose: set of oppose in form of set( strSort('x', 'y'), strSort('a', 'b') )
# combine: hask of combine in form of {strSort('x', 'y'):'z', strSort('a', 'b'):c}
def findList(inList, oppose, combine):
    resList = [inList[0]]
    curIndex = 1
    while curIndex < len(inList):
        cur = inList[curIndex]
        # look for combines
        if len(resList) > 0:
            other = resList[len(resList)-1]
            if strSort(cur, other) in combine:
                resList = resList[:-1]
                cur = combine[strSort(cur, other)]
        # look for opposes
        empty = False
        for i in range(0, len(resList)):
            if strSort(cur, resList[i]) in oppose:
                resList = []
                empty = True
                break
        if not empty:
            resList.append(cur)
        curIndex += 1
    return resList



fin = open("large.in", "r")
fout = open("large.out", "w")

line = fin.readline()
numCases = int(line)

curCase = 1
while curCase <= numCases:
    line = fin.readline()
    elems = line.split()
    numCombines = int(elems[0])
    combines = {}
    for i in range(1, 1 +numCombines):
        curCombine = elems[i]
        combines[strSort(curCombine[0], curCombine[1])] = curCombine[2]
    numOpposes = int(elems[1 + numCombines])
    opposes = set()
    for i in range(2 + numCombines, 2 + numCombines + numOpposes):
        curOppose = elems[i]
        opposes.add(strSort(curOppose[0], curOppose[1]))
    inList = elems[3 + numCombines + numOpposes].strip()
    res = findList(inList, opposes, combines)
    
    fout.write("Case #" + str(curCase) + ": [")
    for i in range(0, len(res)):
        fout.write(res[i])
        if i != len(res) - 1:
            fout.write(', ')
    fout.write("]\n")
    curCase += 1

fout.close()
fin.close()
