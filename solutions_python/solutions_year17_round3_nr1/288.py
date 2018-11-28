import math

def findSolution(pancakes, ordered):
    surfaceSort = sorted(range(len(pancakes)), key=lambda k: math.pi * math.pow(pancakes[k][0], 2))[::-1]
    heightSort = sorted(range(len(pancakes)), key=lambda k: pancakes[k][0] * pancakes[k][1] * math.pi * 2)[::-1]
    #print(surfaceSort)
    #print(heightSort)
    totalSide = 0
    lastSide = pancakes[heightSort[ordered - 1]][0] * pancakes[heightSort[ordered - 1]][1] * math.pi * 2
    for i in range(0, ordered):
        totalSide += pancakes[heightSort[i]][0] * pancakes[heightSort[i]][1] * math.pi * 2
    #print(totalSide)
    #print(lastSide)
    if surfaceSort[0] in heightSort[0:ordered]:
        #print("hit it1: ")
        return str(totalSide + math.pi * math.pow(pancakes[surfaceSort[0]][0], 2))
    else:
        #print("hit it2: ")
        includeIt = totalSide - lastSide + math.pi * math.pow(pancakes[surfaceSort[0]][0], 2) + pancakes[surfaceSort[0]][0] * pancakes[surfaceSort[0]][1] * math.pi * 2
        excludeIt = totalSide
        for i in surfaceSort:
            if i in heightSort[0:ordered]:
                #print("chose " + str(i))
                excludeIt += math.pi * math.pow(pancakes[i][0], 2)
                break
        #print(includeIt)
        #print(excludeIt)
        return str(max(includeIt, excludeIt))

inp = open("A-large.in", "r")
res = open("out1.txt", "w")
cases = int(inp.readline())
for i in range(cases):
    available, ordered = list(map(int, inp.readline().rstrip().split(" ")))
    pancakes = []
    for j in range(available):
        pancakes.append(list(map(int, inp.readline().rstrip().split(" ")))) 
    res.write("Case #" + str(i+1) + ": " + findSolution(pancakes, ordered) + "\n")
    print(i)