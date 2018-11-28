# lol brute force
from collections import Counter

# requires table not be empty
def moveTable(table, maxCakes, amnt):
    newTable = Counter(table)
    maxCDiners = newTable[maxCakes]
    del newTable[maxCakes]
    newTable[maxCakes-amnt] += maxCDiners
    newTable[amnt] += maxCDiners
    return (newTable, maxCDiners)

def decrementTable(table):
    newTable = Counter()
    for key in table.keys():
        newTable[key-1] = table[key]
    if 0 in newTable.keys():
        del newTable[0]
    return newTable

def solveTable(table):
    if not table: return 0
    maxCakes = max(table.keys())
    if (maxCakes > 3): # worth trying to rearrange
        options = []
        options.append((decrementTable(table),1))
        for a in xrange(2,maxCakes/2+1):
            options.append(moveTable(table,maxCakes,a))
        def mapfn((tab,t)):
            return t+solveTable(tab)
        return min(map(mapfn,options))
    else: return maxCakes

ptable = Counter() # key is num of pancakes, val is num of ppl with that many
fin = open('B-pancakes.in', 'r')
fout = open('B-pancakes.out', 'w')
T = int(fin.readline())

for x in xrange(1,T+1):
    ptable = Counter()
    D = int(fin.readline()) # I never use this
    for p in fin.readline().split():
         ptable[int(p)] += 1
    timer = solveTable(ptable)
    fout.write('Case #' + str(x) + ': ' + str(timer) + '\n')

fin.close()
fout.close()
