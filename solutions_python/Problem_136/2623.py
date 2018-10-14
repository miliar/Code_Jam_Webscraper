import sys

numTests = int(sys.stdin.readline())
for i in range (0,numTests):
    line = sys.stdin.readline().split()
    c=float(line[0])
    f=float(line[1])
    x=float(line[2])
    currentCost = x/2
    nextCost = c/2+x/(2+f)
    baseCost = c/2
    numCookieFactory = 1
    while (currentCost>nextCost):
        currentCost = nextCost
        baseCost+= c/(2+numCookieFactory*f)
        numCookieFactory+=1
        nextCost = baseCost+ x/(2+numCookieFactory*f)
        


    print "Case #"+str(i+1)+":",currentCost
