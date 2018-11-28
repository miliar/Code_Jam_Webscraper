inputFile = "A-large.in"
outputFile = "outputA.txt"

f = open(inputFile, "r")
f.readline()
wf = open(outputFile, "w")

def leavesKlet(pancakes):
    if "+++" not in pancakes and "---" not in pancakes:
        return False
    else:
        return True

def leavesOnlyKlets(pancakes, k):
    for i in range(0, len(pancakes), k):
        if pancakes[i:i + k] != "+++" and pancakes[i:i + k] != "---":
            return False
    return True

def isHappy(pancakes):
    if "-" not in pancakes:
        return True
    else:
        return False


def flipPancakes(pancakes, k, index):
    pancakeList = list(pancakes)
    for i in range(index, index + k):
        if pancakeList[i] == '+':
            pancakeList[i] = '-'
        else:
            pancakeList[i] = "+"
    return "".join(pancakeList)

def flipFirstSad(pancakes, k):
    flipCount = 0
    if isHappy(pancakes):
        return 0
    for i in range(0, len(pancakes)):
        if pancakes[i] == '-':
            if (len(pancakes) - i) < k:
                return -1
            else:
                pancakes = flipPancakes(pancakes, k, i)
                flipCount += 1
                if isHappy(pancakes):
                    return flipCount
    return -1

testCase = 1
for line in f:
    pancakes = line.split()[0]
    k = int(line.split()[1])
    minFlips = flipFirstSad(pancakes, k)
    if minFlips != -1:
        wf.write("Case #" + str(testCase) + ": " + str(minFlips) + "\n")
    else:
        wf.write("Case #" + str(testCase) + ": IMPOSSIBLE\n")
    testCase += 1

f.close()
wf.close()