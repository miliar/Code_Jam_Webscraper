import re
import math

fileName = "input.txt"
fileName = "A-small-attempt3.in"
fileName = "A-large.in"
input = open(fileName)
#outputFile = open("output-test.txt", "w")
#outputFile = open("output-small3.txt", "w")
outputFile = open("output-large.txt", "w")

def readLine(stream=input):
    return stream.readline().replace("\r","").replace("\n","")
    
def writeLine(text):
    outputFile.write(str(text).lstrip().rstrip() + "\n")
    print text

def mysort(a,b):
    if a[0] < b[0]:
        return -1
    else:
        return 1
        
T = int(readLine())
for caseIndex in xrange(T):
    N = int(readLine())
    wires = []
    for i in range(N):
        wires.append(map(lambda x: int(x), readLine(input).split(" ")))
    crosses = 0
    wires.sort(mysort)
    
    for i in range(N):
        start,end = wires[i]
        for j in range(i+1,N):
            oStart,oEnd = wires[j]
            #print start,end,oStart,oEnd
            if end > oEnd:
                #print end " > " oStart
                crosses += 1
    writeLine("Case #%d: %d" % (caseIndex+1,crosses))
    