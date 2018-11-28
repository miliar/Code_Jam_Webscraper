import itertools

def good(l, edges):
    for i in range(len(edges)):
        if edges[i] > l[i]:
            return False
    return True

def count(l):
    listCopy = list(l)
    retVal = 0
    while(len(listCopy) > 0):
        indRem = listCopy.index(len(listCopy) - 1)
        retVal += len(listCopy) - 1 - indRem
        listCopy.remove(len(listCopy) - 1)
    return retVal

INPUT_FILE = 'inputs/A-small-attempt0.in'
OUTPUT_FILE = 'outputs/A-small-attempt0.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline().strip())
for i in range(T):
    N = int(f_in.readline().strip())
    matr = []
    for j in range(N):
        matr.append([int(x) for x in list(f_in.readline().strip())])
    edges = [0] * N
    ind = []
    for j in range(N):
        currRow = matr[j]
        currEdge = 0;
        for k in range(N):
            if currRow[k] == 1:
                currEdge = k
        edges[j] = currEdge
        ind.append(j)
    
    allPerms = list(itertools.permutations(ind))
    minCount = 1000000000
    for perm in allPerms:
        if (good(perm, edges)):
            currCount = count(perm)
            if (currCount < minCount):
                minCount = currCount
    print("Case #" + str(i + 1) + ": " + str(minCount))
    f_out.write("Case #" + str(i + 1) + ": " + str(minCount) + "\n")

f_in.close()
f_out.close()
