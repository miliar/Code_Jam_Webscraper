numcases=0
testcases=[]

def readFile(file):
    global numcases
    global testcases
    filetext= open(file, "r")
    numcases= (int)(filetext.readline())
    testcases= []
    for j in range (0,numcases): #upper limit not taken
        line= filetext.readline()
        nums=line.split()
        for i in range(0,2): 
            nums[i]=int(nums[i])
        print nums
        testcases.append(nums)
    print testcases
    return testcases


def findfair(num1,num2):
    count=0
    for num in range(num1,num2+1):
        #print num
        if num==1 or num==4 or num==9 or num==121 or num==484:
            count=count+1
    return count


def checkall(testcases, resultfile):
    rfile=open(resultfile,"w")
    answer=""
    for i in range (0,numcases): 
        output= findfair(testcases[i][0],testcases[i][1])
        answer= answer+ "Case #"+str(i+1)+ ": "+str(output) + "\n"
    rfile.write(answer)



testcases= readFile("C-small-attempt0.in")
checkall(testcases,"resultfair.txt")
