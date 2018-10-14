import re
from math import floor

fileName = "input.txt"
fileName = "A-large.in"
input = open(fileName)
outputFile = open("output-snapper-large.txt", "w")

def readLine(stream=input):
    return stream.readline().replace("\r","").replace("\n","")
    
def writeLine(text):
    outputFile.write(str(text).lstrip().rstrip() + "\n")
    #print text
    
T = int(readLine())
for caseIndex in xrange(T):
    N,K = map(lambda x: int(x), readLine(input).split(" "))
    result = float(K+1)/(2**N)
    if result == int(result):
        state = "ON"
    else:
        state = "OFF"
    #print result, int(result)
    writeLine("Case #%d: %s" % (caseIndex+1,state))