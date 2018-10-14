import sys
def readFile(flname):
    lines = open(flname).read().split("\n")
    outputfl = open("output.txt","w")
    testAmount = int(lines[0])
    for i in range(1,len(lines)-1):
        curTest = lines[i].split(" ")
        (y,z) = solveSpecificRow(int(curTest[0]), int(curTest[1]))
        outputfl.write("Case #"+str(i)+": "+str(y)+" "+str(z)+"\n")
    outputfl.close()
def insertToSortedList(lst,x):
    for i in range(len(lst)):
        if x<= lst[i]:
            lst.insert(i,x)
            return
    lst.append(x)
    
def insertPlayer(locations):
    possibilities=[]# list sorted up by loc of of (loc,ls,rs)
    curLoc = locations[0]
    for i in range(1,len(locations)):
        nextLoc = locations[i]
        for j in range(curLoc+1,nextLoc):
            possibilities.append((j,j-curLoc-1,nextLoc-j-1))
        curLoc = nextLoc
    bestPossibility = sorted(possibilities, key = lambda (loc,ls,rs): (min(ls,rs),max(ls,rs),-loc))[-1]
    (bestLocation,bestls,bestrs) = bestPossibility
    insertToSortedList(locations,bestLocation)
    return (max(bestls,bestrs),min(bestls,bestrs))
def solveSpecificRow(n,k):
    locations = [0,n+1]
    for i in range(k):
        (y,z) = insertPlayer(locations)
    return (y,z)
    
