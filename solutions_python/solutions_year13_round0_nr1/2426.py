import numpy
numcases = 0
testcases = []

# -1 is for O    #imp
# 1 is for X
# -1000 is for  . - no input  - sum of all if > 1000 then not completed
# 100 is for T

def readFile(file):
    global numcases
    global testcases
    filetext= open(file, "r")
    numcases= (int)(filetext.readline())
    testcases= []
    for j in range (0,numcases): #upper limit not taken
        array= numpy.zeros(16).reshape((4, 4))
        for i in range (0,4):
          line= filetext.readline()
          #print str(i)+line
          array[i]=parseLine(line) 
        testcases.append(array)
        blank= filetext.readline()  #one test case done
        #print blank
    return testcases
        #if blank!=0:
        #   print "Error: After test case"+ str(j)+ "blank line not found"


def parseLine(line):
    linearray=[0,0,0,0]
    #print line[0:0+2]
    for i in range (0,4):
        if str(line[i])=="T":
            linearray[i]=100
        elif str(line[i])==".":
            linearray[i]=-1000
        elif str(line[i])=="O":
            linearray[i]=-1
        elif str(line[i])=="X":
            linearray[i]=1
        else:
            print "invalid input"
    return linearray


def check(testcases,resultfile):
    global numcases
    #print testcases 
    rfile=open(resultfile,"w")
    answer=""
    for i in range (1,numcases+1): 
        output= checkcase(testcases[i-1])
        answer= answer+ "Case #"+str(i)+ ": "+output + "\n"
    #last output
    #lastoutput= checkcase(testcases[i-1])
    #answer= answer+ "Case #"+str(i)+ ": "+lastoutput
    rfile.write(answer)

def checkcase(array):
    goingon= 0
    for row in array: 
        sum = 0 
       

        #check rows
        for element in row: 
            sum= sum + element
        #print "row sum"+str(sum)

        if sum==4 or sum==103: 
            return "X won"
        if sum==-4 or sum==97:
            return "O won"
        if sum < -100:
            goingon=1

    #check columns
    for i in range (0,4):
        csum= array[0][i]+ array[1][i]+ array[2][i]+ array[3][i]
        if csum==4 or csum==103: 
            return "X won"
        if csum==-4 or csum==97:
            return "O won"

    #check diagonals

    csum1= array[0][0]+ array[1][1]+ array[2][2]+ array[3][3]
    csum2= array[0][3]+ array[1][2]+ array[2][1]+ array[3][0]

    if csum1==4 or csum1==103 or csum2==4 or csum2==103: 
            return "X won"
    if csum1==-4 or csum1==97 or csum2==-4 or csum2==97:
            return "O won"

    if goingon==1: 
        return "Game has not completed"
    else: 
        return "Draw"



#input file
#testcases= readFile("testfile.txt")
testcases= readFile("LargeA.in")
check(testcases, "resultlarge.txt")


