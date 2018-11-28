from collections import defaultdict
import sys
import math


debug = False

def testCase(ingredients, recipe):
    indexPointer = [0] * len(ingredients)
    if debug: print indexPointer
    totalCount = 0
    while True:
        currentLimit = -1
        partial = float(ingredients[0][indexPointer[0]]) / (recipe[0])
        minTotal, maxTotal = int(math.ceil( partial / 1.1)) ,int(math.floor(partial / .9))
        if minTotal > maxTotal or maxTotal == 0:
            indexPointer[0] += 1
            if indexPointer[0] >= len(ingredients[0]):
                return totalCount
            continue


        if currentLimit != -1 and minTotal > currentLimit:
            indexPointer[0] += 1
            if indexPointer[0] >= len(ingredients[0]):
                return totalCount
            continue


        if debug: print "Outer", minTotal, maxTotal, indexPointer
        success = True
        for i in range(1, len(ingredients)):
            continueOn = True
            while continueOn:
                partial = float(ingredients[i][indexPointer[i]]) / (recipe[i])
                minItem, maxItem = int(math.ceil( partial / 1.1)) ,int(math.floor(partial / .9))
                if debug: print i, indexPointer[i]
                if debug: print minItem, maxItem
                if currentLimit != -1 and minItem > currentLimit:
                    indexPointer[i] += 1
                    if indexPointer[i] >= len(ingredients[i]):
                        return totalCount
                    continue
                #Not a valid item
                if minItem > maxItem or maxTotal == 0:
                    if debug: print "Keith"
                    indexPointer[i] += 1
                    if indexPointer[i] >= len(ingredients[i]):
                        return totalCount
                    continue
                #The largest current is less than the smallest
                if minItem > maxTotal:
                    if debug: print "Keith2"
                    indexPointer[i] += 1
                    if indexPointer[i] >= len(ingredients[i]):
                        return totalCount
                    continue

                #The largest current is less than the smallest
                if maxItem <  minTotal:
                    continueOn = False
                    currentLimit = maxItem
                    success = False
                    continue



                if maxItem <  maxTotal:
                    maxTotal = maxItem

                if minItem < minTotal:
                    minTotal = minItem

                continueOn = False

        if success:
            totalCount += 1
            if debug: print totalCount
            if debug: print indexPointer
            if debug: print "Success"
            for i in range(0, len(ingredients)):
                indexPointer[i] += 1
                if indexPointer[i] >= len(ingredients[i]):
                    return totalCount
                continue
        else:
            indexPointer[0] += 1
            if indexPointer[0] >= len(ingredients[0]):
                return totalCount
            continue







testcount = int(sys.stdin.readline())
for i in range(testcount):
    n,p = map(int, sys.stdin.readline().strip("\n").split(" "))
    recipe = map(int, sys.stdin.readline().strip("\n").split(" "))
    ingredients = []
    for j in range(n):
        ingredients.append(sorted(map(int, sys.stdin.readline().strip("\n").split(" ")),reverse=True))


    #print n,p
    #print recipe
    #print ingredients
    answer = testCase(ingredients, recipe)

    #answer = testCase(int(line))
    print("Case #{}: {}".format(i+1, answer))
