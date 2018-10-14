'''
Created on 27/04/2013

@author: George
'''
import math

testfiles = "A-small-attempt0"
fileIN = open("%s.in" %testfiles)
imput= fileIN.read()
fileIN.close()
f = open("%s_OUT.txt" %testfiles, "a")


class Class():
    def __init__(self):
        pass


lines = imput.split("\n")
countTests = int(lines[0])
iTested = 0
testStartLine = 1

while iTested < countTests:
    #iterate through the tests in input file
    params = lines[testStartLine].split(" ")
    innerRadius = int(params[0])
    paintLevels = int(params[1])
    Pi = math.pi
    circlesDrawn = 0
    
    while paintLevels > 0:
        if circlesDrawn == 0:
            nextRadius = innerRadius + 1

        else:
            nextRadius += 2
        lastR = nextRadius -1 
        nextBlack = nextRadius*nextRadius - lastR*lastR
        if nextBlack <= paintLevels:
            paintLevels -= nextBlack
            LastR = nextRadius
            circlesDrawn += 1
        else:
            #print "too expensive", nextBlack, paintLevels
            break

        

    
    print  >>f, "Case #%s:" %(iTested+1), circlesDrawn
    iTested += 1
    testStartLine += 1



f.close()
print "BULLSEYE DONE!"