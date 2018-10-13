import re
import math

fileName = "input.txt"
fileName = "A-small-attempt0.in"
fileName = "A-large.in"
input = open(fileName)
outputFile = open("output-large.txt", "w")

def readLine(stream=input):
    return stream.readline().replace("\r","").replace("\n","")
    
def writeLine(text):
    outputFile.write(str(text).lstrip().rstrip() + "\n")
    print text

def compare(a,b):
    ac = a.count("/")
    bc = b.count("/")
    
    if ac < bc:
        return -1
    if ac == bc:
        return 0
    return 1
    
T = int(readLine())
for caseIndex in xrange(T):
    N,M = map(lambda x: int(x), readLine(input).split(" "))
    
    exist = {}
    for i in range(N):
        dir = readLine(input)[1:]
        exist[dir] = 1
    
    make = []
    for i in range(M):
        dir = readLine(input)[1:]
        make.append(dir)
    make.sort(compare)
    count = 0
    for d in make:
        start = 0
        while True:
            start = d.find("/",start+1)
            if start == -1:
                break
            sub = d[:start]
            if exist.get(sub,0) != 1:
                count = count + 1
                exist[sub] = 1
        if exist.get(d,0) != 1:
            count = count + 1
            exist[d] = 1
    writeLine("Case #%d: %d" % (caseIndex+1,count))