num = int(input())
for ind in range(1, num+1):
    numCities, numStops = map(int, input().split(" "))
    cityData = []
    for i in range(numCities):
        cityData.append(list(map(int, input().split(" "))))
    adjMatrix = []
    for i in range(numCities):
        adjMatrix.append(list(map(int, input().split(" "))))
    edgeList = [[(i,adjMatrix[j][i]) for i in range(len(adjMatrix[j])) if adjMatrix[j][i]!=-1] for j in range(len(adjMatrix)) ]
    #edgeList =
    for i in range(numStops):
        fromLoc, toLoc = list(map(int, input().split(" ")))
        dyn = [10000000000000000000000 for i in range(fromLoc, toLoc+1)]
        dyn[toLoc-1]=0
        for i in range(toLoc-2,fromLoc-2,-1):
            farthest = i
            ponyDist, ponySpeed = cityData[i]
            distLeft = ponyDist
            bestRoute = 100000000000000000000000000
            while distLeft>=0 and farthest<len(dyn):
                bestRoute = min(bestRoute, float(ponyDist-distLeft)/ponySpeed+dyn[farthest])
                if edgeList[farthest]:
                    distLeft-=edgeList[farthest][0][1]
                farthest+=1
            dyn[i]=bestRoute
        print("Case #%d: %.6f"%(ind, dyn[0]))
