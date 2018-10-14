import string

file_name = "trie.in"

trieInput = open(file_name, 'r')
data = string.split(trieInput.read().strip(), '\n')
numCases = int(data[0])

def countNodes(tries):
    if len(tries) == 0:
        return 0
    nodes = set()
    for word in tries:
        for lenWord in range(len(word)):
            nodes.add(word[:lenWord+1])
    return len(nodes) + 1 # +1 for the empty string

def countWorstCase(numServer, tries):
    maxCost = 0
    count = 0
    for i in range(0, numServer ** len(tries)):
        index = [ [i / (numServer**x) % numServer, x] for x in range(len(tries))]
        cost = 0
        for j in range(numServer):
            serverTries = [tries[k] for k in range(len(tries)) if index[k][0] == j]
            cost += countNodes(serverTries)

        if maxCost < cost:
            maxCost = cost
            count = 1
        elif maxCost == cost:
            count += 1
    return maxCost, count
    


index = 1
for case in range(1,numCases+1):
    numTrie, numServer = [int(x) for x in string.split(data[index])]
    tries = []
    for i in range(index+1, index+numTrie +1):
        tries.append(data[i])
    index +=numTrie +1

    worstCost, numWaysWorstCost = countWorstCase(numServer, tries)
    print "Case #" + str(case)+ ":", worstCost, numWaysWorstCost
