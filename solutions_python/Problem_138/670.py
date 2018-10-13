import sys
from math import sqrt, floor
f = open(sys.argv[1], 'r')

numOfTest = int(f.readline())

for i in range(1, numOfTest + 1) :
    print "Case #" + str(i) + ":",
    
    # read test case
    numBlock = int(f.readline())
    naomiBlocks = []
    kenBlocks = []
    for j in f.readline().split() :
        naomiBlocks.append(float(j))
    for j in f.readline().split() :
        kenBlocks.append(float(j))
    naomiBlocks.sort()
    kenBlocks.sort()
    kenBlocks2 = kenBlocks[:]

    # Deceitful War
    ansDWar = 0
    for naomi in naomiBlocks :
        if naomi < kenBlocks[0] :
            kenBlocks.pop()
        else :
            ansDWar += 1
            kenBlocks = kenBlocks[1:]
    naomiBlocks.reverse()
    kenBlocks2.reverse()
    
    # War
    ansWar = 0
    for naomi in naomiBlocks :
        if naomi > kenBlocks2[0] :
            ansWar += 1
        else :
            kenBlocks2 = kenBlocks2[1:]

    print ansDWar, ansWar
