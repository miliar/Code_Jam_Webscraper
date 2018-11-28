import re
import math

fileName = "input.txt"
fileName = "B-small-attempt0.in"
#fileName = "A-large.in"
input = open(fileName)
outputFile = open("output-small0.txt", "w")

def readLine(stream=input):
    return stream.readline().replace("\r","").replace("\n","")
    
def writeLine(text):
    outputFile.write(str(text).lstrip().rstrip() + "\n")
    print text
    
def needToPass(c,cF,B,T):
    diffV = float(c['v'] - cF['v'])
    if diffV <= 0:
        return False
        
    diffX = float(cF['x'] - c['x'])
    timeToCatch = diffX/diffV
    timeToFinish = (B - c['x'] - c['v']*timeToCatch)/cF['v']
    
    return (timeToCatch + timeToFinish) > T
    
C = int(readLine())
for caseIndex in xrange(C):
    N,K,B,T = map(lambda x: int(x), readLine(input).split(" "))
    
    chix = []
    locs = map(lambda x: int(x), readLine(input).split(" "))
    vels = map(lambda x: int(x), readLine(input).split(" "))
    for i in range(N):
        chix.append({'x':locs[i],'v':vels[i]})
    chix.reverse()
    count,swaps = 0,0
    for i in range(len(chix)):
        #print count,swaps
        newIndex = i
        c = chix[i]
        if float(B - c['x'])/float(c['v']) <= float(T):
            #print "MAKE IT"
            count += 1
            #print range(i-1,-1,-1)
            for j in range(i-1,-1,-1):
                #print c,chix[j]
                if needToPass(c,chix[j],B,T):
                    #print "YES"
                    swaps += 1
                    chix[j],chix[newIndex] = chix[newIndex],chix[j]
                    newIndex = j
                else:
                    5
                    #print "NO"
            if count == K:
                break
    if count >= K:
        writeLine("Case #%d: %d" % (caseIndex+1,swaps))
    else:
        writeLine("Case #%d: %s" % (caseIndex+1,"IMPOSSIBLE"))