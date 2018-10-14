inputFile = open('D-small-attempt0.in', 'r')
outputFile = open('D-small-attempt0.out', 'w')

import itertools
import copy

numTests = int(inputFile.readline())

# Going to try brute force split first
def buildTrie(s):
    if len(s) == 0:
        return {}
    trie = {'':''}
    for word in s:
        prefix = ''
        for letter in word:
            prefix += letter
            if prefix not in trie:
                trie[prefix] = ''
    return trie

 
def generateAllSplits(words, numServs):
    if numServs == 1:
        return [[tuple(words)]]
    else:
        firstServs = []
        splits = []
        for j in range(len(words)+1):
            firstServs += list(itertools.combinations(words, j))
        for f in firstServs:
            remWords = copy.deepcopy(words)
            for w in f:
                remWords.remove(w)
            remSplits = generateAllSplits(remWords, numServs-1)
            splits += map(lambda x: [f]+x, remSplits)
        return splits
            
        

for i in range(numTests):
    print i
    line = map(lambda x: int(x), inputFile.readline().split())
    numWords = line[0]
    numServs = line[1]

    words = []
    for j in range(numWords):
        words += [inputFile.readline().strip()]

    maxSplit = 0
    maxCount = 0
    allSplits = generateAllSplits(words, numServs)

    for split in allSplits:
        numNodes = 0
        for serv in split:
            trie = buildTrie(serv)
            numNodes += len(trie)
        if numNodes > maxSplit:
            maxSplit = numNodes
            maxCount = 1
        elif numNodes == maxSplit:
            maxCount += 1

    outputFile.write('Case #' + str(i+1) + ': ' + str(maxSplit) + ' ' + str(maxCount % 1000000007) + '\n')
    
    


inputFile.close()
outputFile.close()
