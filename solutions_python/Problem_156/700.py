from math import sqrt

def allones(pancakes):
    for p in pancakes:
        if not p == 1:
            return False
    return True

def findMin(pancakes):
    if allones(pancakes):
        return 1
    donothing = max(pancakes)
    maxIndex = -1
    for i in range(0, len(pancakes)):
        if pancakes[i] == donothing:
            maxIndex = i
    
    branches = []
    for i in range(2, int(sqrt(donothing))+1):
        copy = list(pancakes)
        copy[maxIndex] = int(donothing/i)
        copy.append(int(donothing/i) + (donothing % i))
        for j in range(2, i):
            copy.append(int(donothing/i))
        branches.append(findMin(copy) + i - 1)
    
    if len(branches) == 0:
        return donothing
    return min(donothing, min(branches))

if __name__ == "__main__":
    numCases = input()
    for c in range(1, numCases+1):
        D = input()
        pancakes = []
        line = raw_input().split()
        for word in line:
            pancakes.append(int(word))
        print("Case #" + str(c) + ": " + str(findMin(pancakes)))
