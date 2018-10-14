import sys

def calcDpTable(sStartPos, subStartPos, s, sub, dpTable):
    if dpTable[sStartPos][subStartPos] != None:
        return dpTable[sStartPos][subStartPos]
    elif subStartPos == len(sub) - 1:
        return s[sStartPos:].count(sub[-1])
        
    cellValue = 0
    for i, sCh in enumerate(s[sStartPos:]):
        if sCh == sub[subStartPos]:
            cellValue += calcDpTable(sStartPos + i + 1, subStartPos + 1, s, sub, dpTable)
    dpTable[sStartPos][subStartPos] = cellValue
    return cellValue
def countSubsequence(s, sub):
    lenS = len(s)
    lenSub = len(sub)
    dpTable = []
    for i in range(lenS):
        dpTable.append([None] * lenSub)
    calcDpTable(0, 0, s, sub, dpTable)
##    for l in dpTable:
##        print l
    return dpTable[0][0]


sub = 'welcome to code jam'
n = sys.stdin.readline().split()
lines = sys.stdin.readlines()
for i, line in enumerate(lines):
    print 'Case #%d: %04d' %(i+1, countSubsequence(line, sub))
                    

