#!/usr/bin/python
import os, sys, math

def isSolved(chests):
    for chest in chests:
        if not chest[2]:
            return False
    return True


def solve(curKeys, chests, keyMoves):
    if isSolved(chests):
        return keyMoves
    if len(curKeys) == 0:
        return None
    chestsToOpen = [chest for chest in chests if not chest[2]]
    allKeysNeeded = [chest[0] for chest in chestsToOpen]
    allPossibleKeys = curKeys[:]
    for chest in chestsToOpen:
        allPossibleKeys = allPossibleKeys + chest[1]
    maxKey = max(allKeysNeeded)
    for keyNumber in range(1,maxKey+1):
        if allKeysNeeded.count(keyNumber) > allPossibleKeys.count(keyNumber):
            return None
    for chest in chestsToOpen:
        # see if we will never be able to open this chest
        neededKey = chest[0]
        if allPossibleKeys.count(neededKey) - chest[1].count(neededKey) == 0:
            return None
    #numLeftToOpen = len([chest for chest in chests if not chest[2]])
    #numKeysCanGet = sum([len(chest[1]) for chest in chests if not chest[2]])
    #if len(curKeys) + numKeysCanGet < numLeftToOpen:
    #    return None
    # Find all possible moves in lexicographical order and try them
    for (i, chest) in enumerate(chests):
        if not chest[2] and chest[0] in curKeys:
            # try opening
            newKeys = curKeys[:]
            newKeys.remove(chest[0])
            newChests = chests[:]
            newChests[i] = (chest[0], chest[1], True)
            for foundKey in chest[1]:
                newKeys.append(foundKey)
            newMoves = keyMoves[:]
            newMoves.append(i+1)
            solution = solve(newKeys, newChests, newMoves)
            if solution:
                return solution
            # if this doesn't work and we got the same key that we used,
            # it's impossible
            if chest[0] in chest[1]:
                return None


    #print startKeys
    #print chests
    return None

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        #print index
        numStartKeys, numChests = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        startKeys = [int(x) for x in fileLines[index][:-1].split(' ')]
        index += 1
        chests = []
        for i in range(numChests):
            line = [int(x) for x in fileLines[index][:-1].split(' ')]
            index += 1
            neededType = line[0]
            keysInChest = line[2:]
            chests.append((neededType, keysInChest, False))
        #print chests
        answer = solve(startKeys, chests, [])
        answerStr = 'IMPOSSIBLE' if answer is None else ' '.join([str(x) for x in answer])
        #print caseStr
        print "Case #%d: %s" % (caseNum + 1, answerStr)

if __name__ == '__main__':
    main(sys.argv[1])
