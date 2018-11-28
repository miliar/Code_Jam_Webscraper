def readFile(flname):
    lines = open(flname).read().split("\n")
    outputfl = open("output.txt","w")
    testAmount = int(lines[0])
    for i in range(1,len(lines)):
        curTest = lines[i].split(" ")
        curAns = solveSpecificRow(curTest[0], int(curTest[1]))
        outputfl.write("Case #"+str(i)+": "+str(curAns)+"\n")
    outputfl.close()
    
def swap(row,ind):
    if row[ind]=="+":
        row[ind]="-"
    else:
        row[ind]="+"
def swapNextK(row,ind,k):
    for i in range(ind, ind+k):
        swap(row,i)
def solveSpecificRow(row,k):
    row = [x for x in row]
    i=0
    cnt=0
    n=len(row)
    for i in range(n):
        if row[i]=="-":
            if i+k>n:
                return "IMPOSSIBLE"
            swapNextK(row,i,k)
            cnt+=1
    return cnt
