inFile = open("../C-large.in", "r")
outFile = open("../C-sol.txt", "w")

memoDict = {}

def findString(patIndex, strIndex, pattern, string):
    if memoDict.has_key((patIndex, strIndex)):
        return memoDict[(patIndex, strIndex)]
    findCount = 0
    for i in range(strIndex, len(string)):
        if pattern[patIndex] == string[i]:
            if patIndex == (len(pattern) - 1):
                findCount = findCount + 1
            else:
                findCount += findString(patIndex+1, i+1, pattern, string)
    memoDict[(patIndex, strIndex)] = findCount
    return findCount

numCases = int(inFile.readline())

for i in range(numCases):
    word = inFile.readline().strip()
    finalNum = findString(0, 0, "welcome to code jam", word)
    finalSeq = list()
    finalSeq.append((finalNum / 1000) % 10)
    finalSeq.append((finalNum / 100) % 10)
    finalSeq.append((finalNum / 10) % 10)
    finalSeq.append(finalNum % 10)
    outFile.write("Case #" + str(i+1) + ": " + "".join(map(str, finalSeq)) + "\n")
    memoDict.clear()