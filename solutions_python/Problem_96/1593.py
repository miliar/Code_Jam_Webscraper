import sys

def createTriplets(totalPointsList):
    tripletList = [generateTriplet(totalPoint) for totalPoint in totalPointsList ]
    return tripletList

def generateTriplet(totalPoint):
    num = totalPoint/3
    triplet = [num for i in range(3)]
    rem = totalPoint - num*3
    if rem == 2:
        triplet[0] += 1
        triplet[1] += 1
    elif rem == 1:
        triplet[0] += 1
    return triplet

def generateSurpTriplet(totalPoint):
    num = totalPoint/3
    triplet = [num for i in range(3)]
    rem = totalPoint - num*3
    if rem == 2:
        triplet[0] += 2
    elif rem == 1:
        triplet[0] += 1
        triplet[1] += 1
        triplet[2] -= 1
    else:
        #remainder == 0
        triplet[1] += 1
        triplet[2] -= 1
    return triplet


def checkIfSurprise(triplet):
    maxDiff = maxDiffTriplet(triplet)
    if maxDiff == 2:
        return True
    else:
        return False

def maxDiffTriplet(triplet):
    maxDiff = 0
    pair = [0,0]
    if abs(triplet[0] - triplet[1]) > maxDiff:
        maxDiff = abs(triplet[0] - triplet[1])
        pair = [0, 1]
    if abs(triplet[0] - triplet[2]) > maxDiff:
        maxDiff = abs(triplet[0] - triplet[2])
        pair = [0, 2]
    if abs(triplet[2] - triplet[1]) > maxDiff:
        pair = [2, 1]
        maxDiff = abs(triplet[2] - triplet[1])
    return maxDiff, pair

def makeSurprise(triplet):
    if not checkIfSurprise(triplet):
        triplet = generateSurpTriplet(sum(triplet))
    return triplet

def canBeMadeSurprise(triplet, bestScore):
    if sum(triplet) < 29 and sum(triplet) > 0 and sum(triplet)>=(3*bestScore-4)\
            and max(triplet) < bestScore:
        return True
    else:
        return False

def countWithBestResults(tripletsList, bestResult):
    count = 0
    for triplet in tripletsList:
        if max(triplet) >= bestResult:
            count += 1
    return count

def processInputList(ipList):
    numGooglers =  ipList[0]
    numSurTriplets = ipList[1]
    bestScore = ipList[2]
    tripletSums = ipList[3:]
    tripletSums.sort(reverse=True)
    tripletList = createTriplets(tripletSums)
    surpCount = 0
    for i in range(len(tripletList)):
        if surpCount < numSurTriplets:
            triplet = tripletList[i]
            if canBeMadeSurprise(triplet, bestScore):
                surTriplet = makeSurprise(triplet)
                tripletList[i] = surTriplet
                surpCount += 1
        else:
            break;
    return countWithBestResults(tripletList, bestScore)
        

#print processInputList([2, 1, 1, 8, 0])

#ip = sys.stdin
ip = open('/Users/mohit/Downloads/B-large.in', 'r')

numCase = int(ip.readline())

inputLines = []
for i in range(numCase):
    inputLines.append( ip.readline().rstrip('\n'))

for i in range(numCase):
    results = [int(ch) for ch in inputLines[i].split()]
    print 'Case #' + str(i+1) + ': ', processInputList(results)
