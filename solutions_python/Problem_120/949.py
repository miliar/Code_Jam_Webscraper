import numpy
numcases = 0
testcases = []
import math


def readFile(file):
    global numcases
    global testcases
    filetext= open(file, "r")
    numcases= (int)(filetext.readline())
    testcases= []
    for j in range (0,numcases): #upper limit not taken
        line= filetext.readline()
          #print str(i)+line\
        array= line.split()
        for i in range(0,2):
            array[0]=int(array[0])
            array[1]=int(array[1])
        testcases.append(array)
    return testcases

def numPossible(rad,t):
    avail= t
    num=0
    for r in xrange(rad,rad+t,2):
        area= ((r+1)**2 - r**2)
        if avail - area < 0:
            return num
        else:
            num= num+1 
            avail= avail - area 
    return num


def computeAll(testcases,resultfile):
    rfile=open(resultfile,"w")
    answer=""
    for i in range (0,numcases): 
        num= numPossible(testcases[i][0],testcases[i][1])
        answer= answer+ "Case #"+str(i+1)+ ": "+str(num) + "\n"
    rfile.write(answer)




testcases= readFile("small.txt")
computeAll(testcases,"resultrings.txt")