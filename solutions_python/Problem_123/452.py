import math
numCases = int(raw_input(""))

def solve(otherMotes, currSize):
    if len(otherMotes) == 0:
        return 0
    if currSize > otherMotes[0]:
        return solve(otherMotes[1:], currSize + otherMotes[0])
    if currSize + currSize - 1 > otherMotes[0]:
        return 1 + solve(otherMotes[1:], currSize*2 - 1 + otherMotes[0])

    if currSize > 1:
        # Add motes to absorb 0th mote
        k = 0
        nsize = currSize
        while nsize <= otherMotes[0]:
            k += 1
            nsize += nsize - 1
        added = k + solve(otherMotes[1:], nsize + otherMotes[0])
    else:
        added = len(otherMotes)

    if added > len(otherMotes):
        return len(otherMotes)
    return added
        
for z in range(numCases):
    myMote, numMotes = map(int,raw_input("").split())
    otherMotes = map(int, raw_input("").split())
    otherMotes.sort()
    numChanges = 0
    currSize = myMote
    print "Case #%d: %d"%(z+1, solve(otherMotes, currSize))
            
